# Security Notes

## Profile choice

| Profile | Use for sensitive work? | Why |
| --- | --- | --- |
| `daily-gpt55-go-provider-diverse` | No, unless cross-provider sharing is acceptable | Uses OpenCode Go fallbacks. |
| `provider-diverse-safe-gpt54-go` | No, unless cross-provider sharing is acceptable | Avoids GPT-5.5 but still uses Go fallbacks. |
| `openai-only-sensitive` | Better default for sensitive/proprietary work | Same-provider OpenAI fallbacks only. |

## Secret handling

- Never commit real `API_TOKEN`, `apiKey`, `Authorization`, passwords, or private endpoint credentials.
- Prefer environment variables or a secrets manager.
- If a real token was committed or pasted into an AI prompt, rotate it.
- Do not print raw `opencode.json` in reviews. Redact first.

## Dependency pinning

The local config may use `@latest` MCP/plugin packages for convenience. For production or CI, pin versions and maintain a lockfile.
