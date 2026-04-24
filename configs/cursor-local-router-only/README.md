# cursor-local-router-only

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

users who want OpenCode UI/routing over an existing Cursor subscription

## Fit

- Status: template-needs-smoke-test
- Access: Cursor subscription with local router/ACP adapter
- Providers used: cursor-acp, cursor
- Main model: `cursor-acp/auto`
- Small model: `cursor-acp/gpt-5.3-codex-low-fast`
- Routing posture: Cursor local-router only
- Privacy posture: Cursor boundary only; cursor and cursor-acp are local-router transports, not separate provider fallbacks
- Cost posture: subscription/router dependent

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

See ../../README.md and ../../docs/*.md for selection and safety notes.
