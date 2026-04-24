#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
dry_run=0
if [[ "${1:-}" == "--dry-run" ]]; then
  dry_run=1
  shift
fi
profile_dir="${1:?usage: scripts/install_profile.sh [--dry-run] configs/<profile-dir>}"
if [[ ! -f "$profile_dir/opencode.json" || ! -f "$profile_dir/oh-my-openagent.json" ]]; then
  echo "profile must contain opencode.json and oh-my-openagent.json" >&2
  exit 2
fi
python3 "$script_dir/validate_configs.py" "$profile_dir" >/dev/null
config_dir="${OPENCODE_CONFIG_DIR:-$HOME/.config/opencode}"
ts="$(date +%Y%m%d-%H%M%S)"
if [[ "$dry_run" == "1" ]]; then
  echo "Would install $profile_dir to $config_dir with backup suffix $ts"
  for f in opencode.json oh-my-openagent.json; do
    echo "- $profile_dir/$f -> $config_dir/$f"
  done
  exit 0
fi
mkdir -p "$config_dir"
for f in opencode.json oh-my-openagent.json; do
  if [[ -f "$config_dir/$f" ]]; then
    cp "$config_dir/$f" "$config_dir/$f.bak-$ts"
  fi
  cp "$profile_dir/$f" "$config_dir/$f"
  chmod 600 "$config_dir/$f"
done
echo "Installed $profile_dir to $config_dir with backup suffix $ts"
