# Model Rationale

This file records why models appear in the shipped profiles. It is intentionally cautious: model availability, benchmarks, price, and context windows drift.

## OpenAI models

| Model | Why use it | Typical profiles |
| --- | --- | --- |
| `openai/gpt-5.5` | Best local high-reliability lane where OAuth/subscription access is actually executable. | `daily-gpt55-go-provider-diverse`, `gpt55-oauth-openai-only` |
| `openai/gpt-5.4` | Portable API-safe high-quality primary when GPT-5.5 API-key access should not be assumed. | `provider-diverse-safe-gpt54-go`, `openai-only-sensitive` |
| `openai/gpt-5.4-mini` | Small/quick/low-risk lane and budget default. | all OpenAI profiles |

## OpenCode Go models

| Model | Why selected | Typical lane |
| --- | --- | --- |
| `opencode-go/glm-5.1` | Long-horizon autonomous coding and many-step tool use. | `sisyphus`, `go-long-horizon` |
| `opencode-go/kimi-k2.6` | Agentic search, broad exploration, alternate hypotheses. | `go-agentic-search`, research fallbacks |
| `opencode-go/mimo-v2.5-pro` | Large-context/1M-style lane in local metadata. | `go-large-context`, librarian fallback |
| `opencode-go/mimo-v2-pro` | Large-context fallback. | `go-large-context` fallback |
| `opencode-go/mimo-v2-omni` | Multimodal image/audio/video/PDF-style work. | `multimodal-looker`, `go-multimodal` |
| `opencode-go/mimo-v2.5` | Lighter multimodal fallback. | visual/multimodal fallback |
| `opencode-go/minimax-m2.7` | Cheap, fast, batch-friendly default for sweeps. | `go-cheap-sweep`, low-cost profiles |
| `opencode-go/minimax-m2.5` | Older/cheaper fallback. | cheap sweep fallback |
| `opencode-go/qwen3.6-plus` | Fast UI prototype/option generation and lighter large-context work. | `ui-prototype`, UI fallback |
| `opencode-go/qwen3.5-plus` | Cheap low-risk summaries/classification/exploration. | low-cost/explore fallback |
| `opencode-go/kimi-k2.5` | Cheap writing/doc fallback. | writing/document fallback |

## Google/Gemini models

| Model | Why selected | Typical lane |
| --- | --- | --- |
| `google/gemini-3.1-pro-preview` | Strong Gemini-first primary where locally listed/available. | Gemini-only and Gemini+Go profiles |
| `google/gemini-3-pro-preview` | Pro fallback when 3.1 variant is unavailable or busy. | hard fallback |
| `google/gemini-3.1-flash-lite-preview` | Quick/small Gemini lane. | explore, writing, low-risk work |
| `google/gemini-3-flash-preview` | Flash fallback. | quick fallback |

## Cursor local-router models

| Model | Why selected | Typical lane |
| --- | --- | --- |
| `cursor-acp/auto` | Let Cursor's router choose when using a local Cursor/ACP endpoint. | default main |
| `cursor-acp/gpt-5.3-codex-high` | Coding-heavy route in the local Cursor ACP model list. | hard coding |
| `cursor-acp/gpt-5.3-codex-xhigh` | Extra-hard coding/review route. | ultrabrain/momus |
| `cursor-acp/gpt-5.3-codex-low-fast` | Fast small lane. | explore/quick |
| `cursor-acp/opus-4.6-thinking` | Alternative reasoning lane through Cursor routing. | oracle/cursor-opus fallback |

## Non-goals

- Do not use OpenCode Go as a universal GPT replacement.
- Do not use cross-provider fallback for sensitive data unless explicitly accepted.
- Do not treat long-horizon endurance as final patch correctness; final verification should remain strict.
- Do not present un-smoke-tested provider-router profiles as guaranteed current for another machine.
