# opencode-go-only-low-cost

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

bulk summarization, classification, exploration, low-risk docs

## Fit

- Status: template-needs-smoke-test
- Access: OpenCode Go subscription
- Providers used: opencode-go
- Main model: `opencode-go/minimax-m2.7`
- Small model: `opencode-go/qwen3.5-plus`
- Routing posture: cheap sweep first, stronger Go models only as fallback
- Privacy posture: single non-OpenAI provider family
- Cost posture: lowest Go spend / highest request budget

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
opencode run -m opencode-go/minimax-m2.7 --title routing-smoke --dangerously-skip-permissions 'Reply with exactly: OK'
```

## Notes

- Not recommended as final reviewer for complex code.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
