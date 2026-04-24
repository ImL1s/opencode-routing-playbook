# opencode-go-only-balanced

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

users who only have OpenCode Go and want a general-purpose setup

## Fit

- Status: template-needs-smoke-test
- Access: OpenCode Go subscription
- Providers used: opencode-go
- Main model: `opencode-go/glm-5.1`
- Small model: `opencode-go/minimax-m2.7`
- Routing posture: Go specialist split without OpenAI
- Privacy posture: single non-OpenAI provider family
- Cost posture: subscription/Go-budget balanced

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
opencode run -m opencode-go/glm-5.1 --title routing-smoke --dangerously-skip-permissions 'Reply with exactly: OK'
```

## Notes

- Uses GLM/Kimi/MiMo/MiniMax/Qwen by role.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
