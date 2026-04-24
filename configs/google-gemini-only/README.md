# google-gemini-only

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

users with Gemini/Antigravity access but no OpenAI/OpenCode Go

## Fit

- Status: template-needs-smoke-test
- Access: Google AI/Gemini API or Antigravity auth
- Providers used: google
- Main model: `google/gemini-3.1-pro-preview`
- Small model: `google/gemini-3.1-flash-lite-preview`
- Routing posture: Gemini-only, same-provider
- Privacy posture: single Google provider boundary
- Cost posture: depends on Google/Gemini plan

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
opencode run -m google/gemini-3.1-pro-preview --title routing-smoke --dangerously-skip-permissions 'Reply with exactly: OK'
```

## Notes

- Model IDs were locally listed; smoke-test in your environment.
- Custom provider stubs include only the models referenced by this profile; add more only after `opencode models <provider>` confirms them.

See ../../README.md and ../../docs/*.md for selection and safety notes.
