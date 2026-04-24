#!/usr/bin/env bash
set -euo pipefail
profile_dir="${1:?usage: scripts/install_profile.sh configs/<profile-dir>}"
if [[ ! -f "$profile_dir/opencode.json" || ! -f "$profile_dir/oh-my-openagent.json" ]]; then
  echo "profile must contain opencode.json and oh-my-openagent.json" >&2
  exit 2
fi
config_dir="${OPENCODE_CONFIG_DIR:-$HOME/.config/opencode}"
mkdir -p "$config_dir"
ts="$(date +%Y%m%d-%H%M%S)"
for f in opencode.json oh-my-openagent.json; do
  if [[ -f "$config_dir/$f" ]]; then
    cp "$config_dir/$f" "$config_dir/$f.bak-$ts"
  fi
  cp "$profile_dir/$f" "$config_dir/$f"
  chmod 600 "$config_dir/$f"
done
echo "Installed $profile_dir to $config_dir with backup suffix $ts"
