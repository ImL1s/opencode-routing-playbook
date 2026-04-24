# Profile Selection

Use this file when deciding by subscription, API key, or provider boundary.

| Access / subscription | Profile | Status | Providers used | Routing posture | Privacy posture |
| --- | --- | --- | --- | --- | --- |
| OpenAI OAuth / GPT subscription, OpenCode Go subscription | `daily-gpt55-go-provider-diverse` | verified | openai, opencode-go | quality-first daily, provider-diverse fallback | cross-provider; avoid for sensitive repos unless accepted |
| OpenAI OAuth / GPT subscription | `gpt55-oauth-openai-only` | template | openai | quality-first, same-provider only | same provider, but still cloud-hosted |
| OpenAI API key, OpenCode Go subscription | `provider-diverse-safe-gpt54-go` | verified | openai, opencode-go | portable OpenAI API primary, Go fallback/specialists | cross-provider; avoid for sensitive repos unless accepted |
| OpenCode Go subscription, OpenAI API key | `go-first-openai-api-review` | template | opencode-go, openai | OpenCode Go first, OpenAI only as escalation/review fallback | cross-provider; prompts may reach either provider |
| OpenAI API key | `openai-only-sensitive` | verified | openai | same-provider, high-quality portable | best shipped profile for sensitive/proprietary repos when OpenAI is approved |
| OpenAI API key | `openai-api-budget-mini` | template | openai | OpenAI mini-first with GPT-5.4 escalation routes | same provider, but lower-capability default |
| OpenCode Go subscription | `opencode-go-only-balanced` | template | opencode-go | Go specialist split without OpenAI | single non-OpenAI provider family |
| OpenCode Go subscription | `opencode-go-only-low-cost` | template | opencode-go | cheap sweep first, stronger Go models only as fallback | single non-OpenAI provider family |
| OpenCode Go subscription | `opencode-go-only-large-context` | template | opencode-go | 1M/context-window-first | single non-OpenAI provider family |
| OpenCode Go subscription | `opencode-go-only-multimodal` | template | opencode-go | multimodal-first | single non-OpenAI provider family |
| Google AI/Gemini API or Antigravity auth | `google-gemini-only` | template | google | Gemini-only, same-provider | single Google provider boundary |
| Google AI/Gemini API or Antigravity auth, OpenCode Go subscription | `google-gemini-go-provider-diverse` | template | google, opencode-go | Gemini primary, Go specialist/fallback lanes | cross-provider Google/OpenCode Go |
| Cursor subscription with local router/ACP adapter | `cursor-local-router-only` | template | cursor-acp, cursor | Cursor local-router only | Cursor boundary only; cursor and cursor-acp are local-router transports, not separate provider fallbacks |
| Cursor subscription with local router/ACP adapter, OpenCode Go subscription | `cursor-go-provider-diverse` | template | cursor-acp, cursor, opencode-go | Cursor primary, Go specialist/fallback lanes | cross-provider Cursor/OpenCode Go |

## Decision rules

1. **Sensitive repo first:** if code/data must stay inside one approved provider, choose a same-provider profile before optimizing cost.
2. **API portability:** if the user only says "OpenAI API key", prefer `provider-diverse-safe-gpt54-go` or `openai-only-sensitive`; do not assume `openai/gpt-5.5` works by API key.
3. **Go as specialist lane:** choose OpenCode Go when the job benefits from lower cost, long context, multimodal input, or provider-diverse outage fallback.
4. **Go-only variants:** choose balanced for ordinary work, low-cost for sweeps, large-context for huge context, and multimodal for media/document-heavy sessions.
5. **Template profiles:** any profile marked `template` must be smoke-tested on the target machine before being treated as verified.
6. **Local routers:** Cursor profiles require a running local Cursor-compatible endpoint; Gemini profiles require Google/Gemini auth in the local OpenCode environment.
