# google-gemini-go-provider-diverse

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

Gemini-first users who also have Go for CP/context lanes

## Fit

- Status: template-needs-smoke-test
- Access: Google AI/Gemini API or Antigravity auth, OpenCode Go subscription
- Providers used: google, opencode-go
- Main model: `google/gemini-3.1-pro-preview`
- Small model: `google/gemini-3.1-flash-lite-preview`
- Routing posture: Gemini primary, Go specialist/fallback lanes
- Privacy posture: cross-provider Google/OpenCode Go
- Cost posture: use Gemini for reasoning and Go for context/multimodal/cheap sweeps

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

- Good alternative when OpenAI is unavailable or quota constrained.
- Custom provider stubs include only the models referenced by this profile; add more only after `opencode models <provider>` confirms them.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
