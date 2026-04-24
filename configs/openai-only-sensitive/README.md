# openai-only-sensitive

sensitive work where OpenCode Go or other provider fallback is not acceptable

## Fit

- Status: verified-local
- Access: OpenAI API key
- Providers used: openai
- Main model: `openai/gpt-5.4`
- Small model: `openai/gpt-5.4-mini`
- Routing posture: same-provider, high-quality portable
- Privacy posture: best shipped profile for sensitive/proprietary repos when OpenAI is approved
- Cost posture: moderate/high depending on workload

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

- Same-provider fallback only.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
