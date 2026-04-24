# cursor-go-provider-diverse

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

Cursor users who also have OpenCode Go and want cheaper/faster side lanes

## Fit

- Status: template-needs-smoke-test
- Access: Cursor subscription with local router/ACP adapter, OpenCode Go subscription
- Providers used: cursor-acp, cursor, opencode-go
- Main model: `cursor-acp/auto`
- Small model: `cursor-acp/gpt-5.3-codex-low-fast`
- Routing posture: Cursor primary, Go specialist/fallback lanes
- Privacy posture: cross-provider Cursor/OpenCode Go
- Cost posture: use Cursor subscription for core work and Go for CP/context/cheap lanes

## Install

```bash
../../scripts/install_profile.sh .
```

## Validate

```bash
python3 ../../scripts/validate_configs.py .
opencode debug config
```

## Smoke test

```bash
opencode run -m cursor-acp/auto --title routing-smoke --dangerously-skip-permissions 'Reply with exactly: OK'
```

## Notes

- Requires the local Cursor-compatible endpoint to be running.
- Custom provider stubs include only the models referenced by this profile; add more only after `opencode models <provider>` confirms them.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
