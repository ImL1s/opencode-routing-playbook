# provider-diverse-safe-gpt54-go

users with OpenAI API plus OpenCode Go, without assuming GPT-5.5 API availability

## Fit

- Status: verified-local
- Access: OpenAI API key, OpenCode Go subscription
- Providers used: openai, opencode-go
- Main model: `openai/gpt-5.4`
- Small model: `openai/gpt-5.4-mini`
- Routing posture: portable OpenAI API primary, Go fallback/specialists
- Privacy posture: cross-provider; avoid for sensitive repos unless accepted
- Cost posture: balanced

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
opencode run -m openai/gpt-5.4 --title routing-smoke --dangerously-skip-permissions 'Reply with exactly: OK'
```

## Notes

- Portable counterpart to the GPT-5.5 daily profile.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
