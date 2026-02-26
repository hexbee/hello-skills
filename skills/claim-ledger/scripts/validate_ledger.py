#!/usr/bin/env python3
"""Validate Claim Ledger markdown without external dependencies."""

import argparse
import io
import json
import os
import re
import sys


REQUIRED_FIELDS = [
    "id",
    "claim",
    "type",
    "confidence",
    "evidence",
    "sourcegrade",
    "counter",
    "boundary",
    "publishability",
]


def normalize_header(value):
    text = value.strip().lower()
    text = text.replace("claim id", "id")
    text = text.replace("claim_id", "id")
    text = text.replace("conf", "confidence")
    text = text.replace("publish", "publishability")
    text = re.sub(r"\(.*?\)", "", text)
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", text)

    mapping = {
        "id": "id",
        "编号": "id",
        "主张id": "id",
        "claim": "claim",
        "主张": "claim",
        "type": "type",
        "类型": "type",
        "confidence": "confidence",
        "置信度": "confidence",
        "evidence": "evidence",
        "证据": "evidence",
        "证据条目": "evidence",
        "sourcegrade": "sourcegrade",
        "来源等级": "sourcegrade",
        "counter": "counter",
        "反证": "counter",
        "反例": "counter",
        "boundary": "boundary",
        "边界": "boundary",
        "适用边界": "boundary",
        "publishability": "publishability",
        "可发布性": "publishability",
    }
    return mapping.get(text, text)


def parse_markdown_table(lines):
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if "|" not in line:
            i += 1
            continue
        if i + 1 >= len(lines):
            i += 1
            continue

        separator = lines[i + 1].strip()
        if "|" not in separator or "-" not in separator:
            i += 1
            continue

        headers = [x.strip() for x in line.strip("|").split("|")]
        normalized = [normalize_header(x) for x in headers]
        if "id" not in normalized or "claim" not in normalized:
            i += 1
            continue

        rows = []
        j = i + 2
        while j < len(lines):
            row = lines[j].strip()
            if not row.startswith("|") or "|" not in row:
                break
            cells = [x.strip() for x in row.strip("|").split("|")]
            if len(cells) < len(headers):
                cells.extend([""] * (len(headers) - len(cells)))
            row_obj = {}
            k = 0
            while k < len(headers):
                row_obj[normalized[k]] = cells[k] if k < len(cells) else ""
                k += 1
            rows.append(row_obj)
            j += 1
        if rows:
            return normalized, rows
        i += 1
    return [], []


def parse_evidence_cards(text):
    cards = {}
    lines = text.splitlines()
    current = None
    buffer_lines = []

    def flush():
        if current is not None:
            cards[current] = "\n".join(buffer_lines).strip()

    for raw in lines:
        line = raw.strip()
        m = re.match(r"^(E\d{2,3})\s*:?\s*$", line, re.IGNORECASE)
        if m:
            flush()
            current = m.group(1).upper()
            buffer_lines = []
            continue
        if current is not None:
            buffer_lines.append(raw.rstrip())
    flush()
    return cards


def extract_evidence_ids(value):
    found = re.findall(r"\bE\d{2,3}\b", value.upper())
    ordered = []
    seen = set()
    for item in found:
        if item not in seen:
            ordered.append(item)
            seen.add(item)
    return ordered


def has_failure_condition(boundary):
    text = boundary.strip().lower()
    if not text:
        return False
    failure_tokens = [
        "失效",
        "不成立",
        "失败",
        "不适用",
        "除非",
        "otherwise",
        "unless",
        "fails",
        "not valid",
    ]
    for token in failure_tokens:
        if token in text:
            return True
    return False


def has_success_condition(boundary):
    text = boundary.strip().lower()
    if not text:
        return False
    success_tokens = ["成立", "适用", "条件", "when", "if", "under"]
    for token in success_tokens:
        if token in text:
            return True
    return False


def is_predictive_or_advice(type_value):
    text = type_value.strip().lower()
    return (
        "预测" in text
        or "建议" in text
        or "prediction" in text
        or "forecast" in text
        or "recommendation" in text
        or "advice" in text
    )


def validate_rows(headers, rows, evidence_cards, strict_mode):
    results = []
    global_issues = []

    missing_headers = [h for h in REQUIRED_FIELDS if h not in headers]
    if missing_headers:
        global_issues.append(
            "Missing required columns: " + ", ".join(missing_headers)
        )

    if len(rows) < 3:
        global_issues.append("Claim count is less than 3.")

    for row in rows:
        claim_id = row.get("id", "").strip() or "UNKNOWN"
        issues = []
        warnings = []

        evidence_ids = extract_evidence_ids(row.get("evidence", ""))
        if len(evidence_ids) < 2:
            issues.append("Evidence count < 2.")

        counter = row.get("counter", "").strip()
        if not counter:
            issues.append("Counter is required.")

        boundary = row.get("boundary", "").strip()
        if not boundary:
            issues.append("Boundary is required.")
        else:
            if not has_success_condition(boundary):
                warnings.append("Boundary may be missing success condition.")
            if not has_failure_condition(boundary):
                issues.append("Boundary is missing failure condition.")

        if is_predictive_or_advice(row.get("type", "")) and not has_failure_condition(boundary):
            issues.append("Predictive/advice claim must include failure condition.")

        if strict_mode:
            missing_cards = []
            for e_id in evidence_ids:
                if e_id not in evidence_cards:
                    missing_cards.append(e_id)
            if missing_cards:
                issues.append(
                    "Missing evidence cards: " + ", ".join(missing_cards)
                )

        results.append(
            {
                "claim_id": claim_id,
                "valid": len(issues) == 0,
                "issues": issues,
                "warnings": warnings,
                "evidence_ids": evidence_ids,
            }
        )

    return global_issues, results


def load_text(path):
    if not os.path.exists(path):
        print("File not found: {0}".format(path), file=sys.stderr)
        sys.exit(2)
    with io.open(path, "r", encoding="utf-8") as f:
        return f.read()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Validate Claim Ledger markdown files."
    )
    parser.add_argument("--file", required=True, help="Path to markdown ledger file.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Require all referenced E## evidence cards to exist in file.",
    )
    parser.add_argument("--json", action="store_true", help="Output JSON.")
    return parser.parse_args()


def main():
    args = parse_args()
    text = load_text(args.file)
    lines = text.splitlines()

    headers, rows = parse_markdown_table(lines)
    evidence_cards = parse_evidence_cards(text)
    global_issues, results = validate_rows(headers, rows, evidence_cards, args.strict)

    all_valid = len(global_issues) == 0 and all(item["valid"] for item in results)
    payload = {
        "file": args.file,
        "valid": all_valid,
        "global_issues": global_issues,
        "claims": results,
        "evidence_card_count": len(evidence_cards),
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=True, indent=2))
        return

    print("Claim Ledger Validation: {0}".format("PASS" if all_valid else "FAIL"))
    print("File: {0}".format(args.file))
    if global_issues:
        print("Global issues:")
        for issue in global_issues:
            print("  - {0}".format(issue))

    for item in results:
        status = "PASS" if item["valid"] else "FAIL"
        print("[{0}] {1}".format(status, item["claim_id"]))
        if item["evidence_ids"]:
            print("  Evidence: {0}".format(", ".join(item["evidence_ids"])))
        if item["warnings"]:
            for warning in item["warnings"]:
                print("  WARN: {0}".format(warning))
        if item["issues"]:
            for issue in item["issues"]:
                print("  - {0}".format(issue))

    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()
