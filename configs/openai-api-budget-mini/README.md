# openai-api-budget-mini

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

OpenAI API users optimizing cost for low-risk repos/tasks

## Fit

- Status: template-needs-smoke-test
- Access: OpenAI API key
- Providers used: openai
- Main model: `openai/gpt-5.4-mini`
- Small model: `openai/gpt-5.4-mini`
- Routing posture: OpenAI mini-first with GPT-5.4 escalation routes
- Privacy posture: same provider, but lower-capability default
- Cost posture: lower OpenAI spend

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
opencode run -m openai/gpt-5.4-mini --title routing-smoke --dangerously-skip-permissions 'Reply with exactly: OK'
```

## Notes

- Keep hard-review categories on GPT-5.4; do not use as final authority for high-risk changes.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
