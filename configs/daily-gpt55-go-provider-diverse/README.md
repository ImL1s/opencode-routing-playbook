# daily-gpt55-go-provider-diverse

daily local workflow when GPT-5.5 is actually executable and OpenCode Go is available

## Fit

- Status: verified-local
- Access: OpenAI OAuth / GPT subscription, OpenCode Go subscription
- Providers used: openai, opencode-go
- Main model: `openai/gpt-5.5`
- Small model: `openai/gpt-5.4-mini`
- Routing posture: quality-first daily, provider-diverse fallback
- Privacy posture: cross-provider; avoid for sensitive repos unless accepted
- Cost posture: uses GPT for high-reliability work and Go for specialist/CP lanes

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
opencode run -m openai/gpt-5.5 --title routing-smoke --dangerously-skip-permissions 'Reply with exactly: OK'
```

## Notes

- Current machine profile from the originating session.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
