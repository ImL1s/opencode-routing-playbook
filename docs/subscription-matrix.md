# Subscription and API Matrix

This matrix is organized by what the user has, not by model hype. All configs are sanitized templates; smoke-test on the target machine.

For rough percentage ranges against pure Claude Opus 4.7, use [`opus47-relative-estimates.md`](opus47-relative-estimates.md). That comparison is docs-only and does not change the installable routing profiles.

| Subscription/API combo | Recommended profile | Status | Main / small | Cost posture | Cross-provider? | Use when |
| --- | --- | --- | --- | --- | --- | --- |
| OpenAI OAuth / GPT subscription + OpenCode Go subscription | `daily-gpt55-go-provider-diverse` | verified | `openai/gpt-5.5` / `openai/gpt-5.4-mini` | uses GPT for high-reliability work and Go for specialist/CP lanes | yes | daily local workflow when GPT-5.5 is actually executable and OpenCode Go is available |
| OpenAI OAuth / GPT subscription | `gpt55-oauth-openai-only` | template | `openai/gpt-5.5` / `openai/gpt-5.4-mini` | subscription/OAuth oriented; no OpenCode Go fallback | no | ChatGPT/Codex-style OAuth users who can run GPT-5.5 but do not want cross-provider routing |
| OpenAI API key + OpenCode Go subscription | `provider-diverse-safe-gpt54-go` | verified | `openai/gpt-5.4` / `openai/gpt-5.4-mini` | balanced | yes | users with OpenAI API plus OpenCode Go, without assuming GPT-5.5 API availability |
| OpenCode Go subscription + OpenAI API key | `go-first-openai-api-review` | template | `opencode-go/glm-5.1` / `opencode-go/minimax-m2.7` | minimize OpenAI API spend while keeping quality escape hatches | yes | users with small OpenAI API budget and cheap Go capacity |
| OpenAI API key | `openai-only-sensitive` | verified | `openai/gpt-5.4` / `openai/gpt-5.4-mini` | moderate/high depending on workload | no | sensitive work where OpenCode Go or other provider fallback is not acceptable |
| OpenAI API key | `openai-api-budget-mini` | template | `openai/gpt-5.4-mini` / `openai/gpt-5.4-mini` | lower OpenAI spend | no | OpenAI API users optimizing cost for low-risk repos/tasks |
| OpenCode Go subscription | `opencode-go-only-balanced` | template | `opencode-go/glm-5.1` / `opencode-go/minimax-m2.7` | subscription/Go-budget balanced | no | users who only have OpenCode Go and want a general-purpose setup |
| OpenCode Go subscription | `opencode-go-only-low-cost` | template | `opencode-go/minimax-m2.7` / `opencode-go/qwen3.5-plus` | lowest Go spend / highest request budget | no | bulk summarization, classification, exploration, low-risk docs |
| OpenCode Go subscription | `opencode-go-only-large-context` | template | `opencode-go/mimo-v2.5-pro` / `opencode-go/qwen3.6-plus` | spend Go quota where huge context matters | no | large repo sweeps, big logs, long documents, context-heavy audits |
| OpenCode Go subscription | `opencode-go-only-multimodal` | template | `opencode-go/mimo-v2-omni` / `opencode-go/minimax-m2.7` | spend Go quota where image/audio/video/PDF context matters | no | vision-heavy, media-heavy, and document-understanding workflows |
| Google AI/Gemini API or Antigravity auth | `google-gemini-only` | template | `google/gemini-3.1-pro-preview` / `google/gemini-3.1-flash-lite-preview` | depends on Google/Gemini plan | no | users with Gemini/Antigravity access but no OpenAI/OpenCode Go |
| Google AI/Gemini API or Antigravity auth + OpenCode Go subscription | `google-gemini-go-provider-diverse` | template | `google/gemini-3.1-pro-preview` / `google/gemini-3.1-flash-lite-preview` | use Gemini for reasoning and Go for context/multimodal/cheap sweeps | yes | Gemini-first users who also have Go for CP/context lanes |
| Cursor subscription with local router/ACP adapter | `cursor-local-router-only` | template | `cursor-acp/auto` / `cursor-acp/gpt-5.3-codex-low-fast` | subscription/router dependent | no | users who want OpenCode UI/routing over an existing Cursor subscription |
| Cursor subscription with local router/ACP adapter + OpenCode Go subscription | `cursor-go-provider-diverse` | template | `cursor-acp/auto` / `cursor-acp/gpt-5.3-codex-low-fast` | use Cursor subscription for core work and Go for CP/context/cheap lanes | yes | Cursor users who also have OpenCode Go and want cheaper/faster side lanes |

## Adding a new combo

1. Run `opencode auth list` and `opencode models <provider>` locally.
2. Create `configs/<profile-name>/opencode.json` and `configs/<profile-name>/oh-my-openagent.json`.
3. Add the profile to `profiles.json` with provider, privacy, cost, and verification posture.
4. Run `python3 scripts/validate_configs.py` from repo root.
5. Smoke-test the main and small model in the real environment.
6. Document any unverified assumptions in the profile README.
