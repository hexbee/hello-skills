#!/usr/bin/env python3
from __future__ import print_function

import argparse
import collections
import datetime
import json
import os
import re
import socket
import sys

try:
    from urllib.error import HTTPError, URLError
    from urllib.parse import quote, urlencode, urlparse
    from urllib.request import Request, urlopen
except ImportError:  # pragma: no cover
    from urllib2 import HTTPError, URLError, Request, urlopen
    from urllib import quote, urlencode
    from urlparse import urlparse


DEFAULT_TIMEOUT = 30
SERVICE_URL = "https://markdown.new/"
USER_AGENT = "url-to-md/1.0 (+https://markdown.new/)"
ConversionResult = collections.namedtuple(
    "ConversionResult",
    ["markdown", "headers", "status", "transport", "service_url"],
)


class MarkdownServiceError(Exception):
    pass


def _normalize_headers(headers):
    normalized = {}
    for key, value in headers.items():
        normalized[str(key).lower()] = value
    return normalized


def _decode_response(response):
    headers = _normalize_headers(response.headers)
    content_type = headers.get("content-type", "")
    charset = "utf-8"

    match = re.search(r"charset=([A-Za-z0-9._-]+)", content_type)
    if match:
        charset = match.group(1)

    body = response.read()
    try:
        text = body.decode(charset, "replace")
    except LookupError:
        text = body.decode("utf-8", "replace")

    if "application/json" in content_type:
        try:
            payload = json.loads(text)
        except ValueError:
            return text, headers
        if isinstance(payload, dict):
            if payload.get("success") is False and payload.get("error"):
                raise MarkdownServiceError(str(payload.get("error")))
            if "content" in payload and payload.get("content") is not None:
                return payload.get("content"), headers
        return text, headers

    return text, headers


def _build_get_request(url, method, retain_images):
    query = urlencode(
        {
            "method": method,
            "retain_images": "true" if retain_images else "false",
        }
    )
    service_url = SERVICE_URL + quote(url, safe=":/")
    if query:
        service_url += "?" + query
    return Request(
        service_url,
        headers={
            "Accept": "text/markdown",
            "User-Agent": USER_AGENT,
        },
    ), service_url


def _build_post_request(url, method, retain_images):
    payload = json.dumps(
        {
            "url": url,
            "method": method,
            "retain_images": bool(retain_images),
        }
    ).encode("utf-8")
    return Request(
        SERVICE_URL,
        data=payload,
        headers={
            "Accept": "text/markdown",
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
        },
    ), SERVICE_URL


def _execute_request(request, transport, timeout, service_url):
    try:
        response = urlopen(request, timeout=timeout)
        markdown, headers = _decode_response(response)
        return ConversionResult(
            markdown=markdown,
            headers=headers,
            status=getattr(response, "status", response.getcode()),
            transport=transport,
            service_url=service_url,
        )
    except HTTPError as exc:
        body = exc.read()
        try:
            detail = body.decode("utf-8", "replace").strip()
        except Exception:
            detail = ""
        message = "HTTP {0} from markdown.new".format(exc.code)
        if exc.code == 429:
            message += " (rate limit exceeded)"
        if detail:
            message += ": " + detail
        raise MarkdownServiceError(message)
    except URLError as exc:
        reason = getattr(exc, "reason", exc)
        raise MarkdownServiceError("Network error contacting markdown.new: {0}".format(reason))
    except socket.timeout:
        raise MarkdownServiceError("Request to markdown.new timed out after {0}s".format(timeout))


def fetch_markdown(url, method="auto", retain_images=False, timeout=DEFAULT_TIMEOUT, transport="auto"):
    if not url:
        raise ValueError("url is required")
    if method not in ("auto", "ai", "browser"):
        raise ValueError("method must be one of: auto, ai, browser")
    if transport not in ("auto", "get", "post"):
        raise ValueError("transport must be one of: auto, get, post")

    if transport == "get":
        request, service_url = _build_get_request(url, method, retain_images)
        return _execute_request(request, "get", timeout, service_url)

    if transport == "post":
        request, service_url = _build_post_request(url, method, retain_images)
        return _execute_request(request, "post", timeout, service_url)

    request, service_url = _build_get_request(url, method, retain_images)
    try:
        return _execute_request(request, "get", timeout, service_url)
    except MarkdownServiceError as exc:
        if "HTTP 429" in str(exc):
            raise
        request, service_url = _build_post_request(url, method, retain_images)
        return _execute_request(request, "post", timeout, service_url)


def _slugify_target(url):
    parsed = urlparse(url)
    host = parsed.netloc or "document"
    path = parsed.path.strip("/")
    if path:
        path = path.replace("/", "-")
        slug = host + "-" + path
    else:
        slug = host
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", slug)
    slug = slug.strip("._-")
    return slug or "document"


def build_output_path(output_value, source_url, now=None):
    if not output_value:
        raise ValueError("output_value is required")

    if now is None:
        now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d-%H%M%S")
    default_base = _slugify_target(source_url)

    is_directory = False
    if os.path.isdir(output_value):
        is_directory = True
    elif output_value.endswith(os.sep):
        is_directory = True
    elif os.altsep and output_value.endswith(os.altsep):
        is_directory = True

    if is_directory:
        directory = output_value
        filename = "{0}-{1}.md".format(default_base, timestamp)
        return os.path.join(directory, filename)

    root, ext = os.path.splitext(output_value)
    if not root:
        root = output_value
    if not ext:
        ext = ".md"
    return "{0}-{1}{2}".format(root, timestamp, ext)


def _write_output(path, content):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    handle = open(path, "w")
    try:
        handle.write(content)
    finally:
        handle.close()


def _print_headers(headers):
    preferred = [
        "content-type",
        "x-markdown-tokens",
        "x-rate-limit-remaining",
        "x-rate-limit-reset",
    ]
    seen = set()
    for key in preferred:
        if key in headers:
            print("{0}: {1}".format(key, headers[key]), file=sys.stderr)
            seen.add(key)
    for key in sorted(headers):
        if key.startswith("x-") and key not in seen:
            print("{0}: {1}".format(key, headers[key]), file=sys.stderr)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert a public URL to Markdown using markdown.new.",
    )
    parser.add_argument("url", help="Public URL to convert")
    parser.add_argument(
        "--method",
        choices=["auto", "ai", "browser"],
        default="auto",
        help="Conversion method exposed by markdown.new (default: auto)",
    )
    parser.add_argument(
        "--retain-images",
        action="store_true",
        help="Request Markdown that keeps image references",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT,
        help="Request timeout in seconds (default: 30)",
    )
    parser.add_argument(
        "--transport",
        choices=["auto", "get", "post"],
        default="auto",
        help="How this client talks to markdown.new (default: auto)",
    )
    parser.add_argument(
        "--output",
        help="Write to a timestamped file. The timestamp is always appended before the extension.",
    )
    parser.add_argument(
        "--show-headers",
        action="store_true",
        help="Print selected response headers to stderr",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    try:
        result = fetch_markdown(
            url=args.url,
            method=args.method,
            retain_images=args.retain_images,
            timeout=args.timeout,
            transport=args.transport,
        )
    except (MarkdownServiceError, ValueError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    if args.show_headers:
        _print_headers(result.headers)

    if args.output:
        output_path = build_output_path(args.output, args.url)
        _write_output(output_path, result.markdown)
        print(output_path, file=sys.stderr)
        return 0

    if result.markdown:
        sys.stdout.write(result.markdown)
        if not result.markdown.endswith("\n"):
            sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
