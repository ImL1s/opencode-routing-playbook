# opencode-go-only-multimodal

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

vision-heavy, media-heavy, and document-understanding workflows

## Fit

- Status: template-needs-smoke-test
- Access: OpenCode Go subscription
- Providers used: opencode-go
- Main model: `opencode-go/mimo-v2-omni`
- Small model: `opencode-go/minimax-m2.7`
- Routing posture: multimodal-first
- Privacy posture: single non-OpenAI provider family
- Cost posture: spend Go quota where image/audio/video/PDF context matters

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
opencode run -m opencode-go/mimo-v2-omni --title routing-smoke --dangerously-skip-permissions 'Reply with exactly: OK'
```

## Notes

- Use balanced Go profile for ordinary text/code work.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
