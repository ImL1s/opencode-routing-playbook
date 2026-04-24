# gpt55-oauth-openai-only

> **Status:** template only; not locally smoke-tested in the originating environment. Re-run `opencode models <provider>` and the smoke command before relying on it.

ChatGPT/Codex-style OAuth users who can run GPT-5.5 but do not want cross-provider routing

## Fit

- Status: template-needs-smoke-test
- Access: OpenAI OAuth / GPT subscription
- Providers used: openai
- Main model: `openai/gpt-5.5`
- Small model: `openai/gpt-5.4-mini`
- Routing posture: quality-first, same-provider only
- Privacy posture: same provider, but still cloud-hosted
- Cost posture: subscription/OAuth oriented; no OpenCode Go fallback

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

- Use only where openai/gpt-5.5 is locally executable; API-key availability is not assumed.
- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers and are not declared as custom provider blocks in `opencode.json`.

See ../../README.md and ../../docs/*.md for selection and safety notes.
