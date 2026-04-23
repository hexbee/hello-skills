#!/usr/bin/env bash

set -u

section() {
  printf '\n== %s ==\n' "$1"
}

run() {
  printf '\n$ %s\n' "$*"
  "$@" 2>&1 || printf '[exit %s]\n' "$?"
}

run_shell() {
  printf '\n$ %s\n' "$*"
  sh -c "$*" 2>&1 || printf '[exit %s]\n' "$?"
}

find_network_services() {
  networksetup -listallnetworkservices 2>/dev/null \
    | sed '1d' \
    | sed 's/^*//'
}

print_service_proxy() {
  service="$1"
  printf '\n-- %s --\n' "$service"
  networksetup -getwebproxy "$service" 2>&1 | sed 's/^/HTTP: /'
  networksetup -getsecurewebproxy "$service" 2>&1 | sed 's/^/HTTPS: /'
}

section "Versions and Context"
run docker version
run_shell "docker info | sed -n '1,120p'"
run orb version
run docker context ls

section "OrbStack Configuration"
run orb config get network_proxy
run_shell "test -f ~/.orbstack/config/docker.json && sed -n '1,160p' ~/.orbstack/config/docker.json || true"
run_shell "test -f ~/.docker/config.json && sed -n '1,160p' ~/.docker/config.json || true"

section "macOS Proxy Settings"
if command -v networksetup >/dev/null 2>&1; then
  services="$(find_network_services)"
  if [ -n "$services" ]; then
    printf '%s\n' "$services" | while IFS= read -r service; do
      [ -n "$service" ] && print_service_proxy "$service"
    done
  else
    print_service_proxy "Wi-Fi"
  fi
else
  printf 'networksetup not found\n'
fi

section "Proxy Processes and Common Ports"
run_shell "ps aux | grep -Ei 'clash|cyberclash|mihomo|sing-box|surge|stash|v2ray|xray|shadow|quantum|loon|proxy' | grep -v grep || true"
run_shell "lsof -nP -iTCP -sTCP:LISTEN | grep -E ':(7890|7897|7899|1080|1087|20171|6152|8080|9090|8888) ' || true"

section "DNS and TUN Clues"
run dscacheutil -q host -a name registry-1.docker.io
run dscacheutil -q host -a name auth.docker.io
run_shell "dig registry-1.docker.io 2>/dev/null | sed -n '1,80p' || true"
run_shell "netstat -rn -f inet | grep -E '198\\.18|default|utun|bridge' || true"
run_shell "ifconfig | grep -E '^[a-z0-9]+:|198\\.18|utun|inet ' || true"

section "Registry Connectivity"
run curl -I --max-time 20 https://auth.docker.io
run curl -I --max-time 20 https://registry-1.docker.io
run curl -I --max-time 20 https://registry-1.docker.io/v2/

section "Explicit Proxy Connectivity"
proxy_url="$(orb config get network_proxy 2>/dev/null || true)"
case "$proxy_url" in
  http://*|https://*)
    run curl -x "$proxy_url" -I --max-time 20 https://registry-1.docker.io/v2/
    ;;
  *)
    printf 'OrbStack network_proxy is not an explicit URL: %s\n' "$proxy_url"
    ;;
esac

section "Docker Pull Smoke Test"
run docker pull hello-world:latest

section "Recent Docker Daemon Logs"
run_shell "orb logs docker | tail -80"

section "Summary Hints"
cat <<'EOF'
- auth.docker.io root 404 and registry root 404 are normal.
- registry-1.docker.io/v2/ should return 401 with a Bearer challenge.
- 198.18.0.x DNS answers usually mean fake-ip/TUN proxy mode.
- If explicit proxy curl works but docker pull EOFs, set OrbStack explicitly:
  orb config set network_proxy http://127.0.0.1:<port>
  orb restart docker
- If large pulls still hang/EOF, preserve existing JSON and add:
  "max-concurrent-downloads": 1
EOF
