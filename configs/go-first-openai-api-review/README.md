# go-first-openai-api-review

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

users with small OpenAI API budget and cheap Go capacity

## Fit

- Status: template-needs-smoke-test
- Access: OpenCode Go subscription, OpenAI API key
- Providers used: opencode-go, openai
- Main model: `opencode-go/glm-5.1`
- Small model: `opencode-go/minimax-m2.7`
- Routing posture: OpenCode Go first, OpenAI only as escalation/review fallback
- Privacy posture: cross-provider; prompts may reach either provider
- Cost posture: minimize OpenAI API spend while keeping quality escape hatches

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

- Good when GPT/API quota is precious but final escalation matters.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
