# Model Rationale

## GPT models

| Model | Why use it |
| --- | --- |
| `openai/gpt-5.5` | Local daily high-reliability primary where available through OpenAI OAuth / Codex-style access. Best for hard coding, architecture, review, and final synthesis. |
| `openai/gpt-5.4` | API-safe/portable high-quality primary when GPT-5.5 availability cannot be assumed. |
| `openai/gpt-5.4-mini` | Standard small model for quick work, lightweight agents, low-risk docs/explore tasks. |

## OpenCode Go models

| Model | Why selected | Typical lane |
| --- | --- | --- |
| `opencode-go/glm-5.1` | Long-horizon autonomous coding and many-step tool use. | `sisyphus`, `go-long-horizon` |
| `opencode-go/kimi-k2.6` | Agentic search, broad exploration, alternate hypotheses. | `go-agentic-search` |
| `opencode-go/mimo-v2.5-pro` | 1M context in local OpenCode Go metadata. | `go-large-context`, librarian fallback |
| `opencode-go/mimo-v2-pro` | 1M context fallback. | `go-large-context` fallback |
| `opencode-go/mimo-v2-omni` | Real multimodal work: image/audio/video/PDF style inputs. | `multimodal-looker`, `go-multimodal` |
| `opencode-go/mimo-v2.5` | Lighter multimodal fallback. | multimodal / visual fallback |
| `opencode-go/minimax-m2.7` | Cheap, fast, good for batch sweeps. | `go-cheap-sweep`, quick fallback |
| `opencode-go/minimax-m2.5` | Cheaper/older fallback. | cheap sweep fallback |
| `opencode-go/qwen3.6-plus` | Fast frontend/UI prototype and option generation. | `ui-prototype`, UI fallback |
| `opencode-go/qwen3.5-plus` | Cheap low-risk summaries/classification/exploration. | `unspecified-low`, explore fallback |
| `opencode-go/kimi-k2.5` | Cheap writing/doc fallback. | writing/document fallback |

## Non-goals

- Do not use OpenCode Go as a universal replacement for GPT.
- Do not use cross-provider fallback for sensitive data unless the user explicitly accepts that boundary.
- Do not treat long-horizon endurance as final patch correctness; final verification should remain strict.
