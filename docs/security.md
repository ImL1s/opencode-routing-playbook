# Security Notes

## Profile choice by provider boundary

| Boundary | Safer profile choices | Avoid unless accepted |
| --- | --- | --- |
| OpenAI-approved only | `openai-only-sensitive`, `gpt55-oauth-openai-only` | Any `*-provider-diverse` or `opencode-go-*` profile |
| Google-approved only | `google-gemini-only` | Gemini+Go, OpenAI+Go, Cursor+Go |
| Cursor/local-router only | `cursor-local-router-only` | Cursor+Go, OpenAI/Google direct routes |
| OpenCode Go only | `opencode-go-only-balanced` and specialist variants | OpenAI/Gemini/Cursor fallbacks |
| Cross-provider OK | provider-diverse profiles | Still avoid secrets in prompts/configs |

## Secret handling

- Never commit real `API_TOKEN`, `apiKey`, `Authorization`, passwords, private keys, cookies, or private endpoint credentials.
- Keep real values in environment variables or a secrets manager.
- If a real token was committed or pasted into an AI prompt, rotate it.
- Do not print raw local `opencode.json` in issues, PRs, or model prompts. Redact first.

## Cross-provider risk

`fallback_models` can move a task to another provider when the primary fails or is overloaded. That is useful for reliability but risky for proprietary code, customer data, credentials, health/finance/legal material, and compliance-bound repos.

For sensitive repos, choose same-provider profiles and keep custom provider blocks minimal.

## MCP risk

The shipped profiles do not bundle BrightData/Firebase/Playwright/Mobile MCP servers by default. Add those locally only after choosing the model profile and accepting the extra tool/API surface.

## Dependency pinning

The templates may use `@latest` plugin packages for convenience. For production or CI, pin versions and maintain a lockfile.
