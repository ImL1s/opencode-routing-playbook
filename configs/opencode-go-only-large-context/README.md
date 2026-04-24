# opencode-go-only-large-context

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

large repo sweeps, big logs, long documents, context-heavy audits

## Fit

- Status: template-needs-smoke-test
- Access: OpenCode Go subscription
- Providers used: opencode-go
- Main model: `opencode-go/mimo-v2.5-pro`
- Small model: `opencode-go/qwen3.6-plus`
- Routing posture: 1M/context-window-first
- Privacy posture: single non-OpenAI provider family
- Cost posture: spend Go quota where huge context matters

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
opencode run -m opencode-go/mimo-v2.5-pro --title routing-smoke --dangerously-skip-permissions 'Reply with exactly: OK'
```

## Notes

- Prefer only when context size is the binding constraint.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
