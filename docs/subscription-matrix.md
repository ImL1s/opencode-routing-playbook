# Subscription Matrix

This is a starter matrix. Add new profiles as actual local availability and pricing are verified.

| Subscription combo | Recommended profile | Notes |
| --- | --- | --- |
| GPT subscription/OAuth + OpenCode Go | `daily-gpt55-go-provider-diverse` | Current local daily setup. GPT-5.5 primary; Go specialist/fallback lanes. |
| OpenAI API key + OpenCode Go | `provider-diverse-safe-gpt54-go` | GPT-5.4 primary because GPT-5.5 API availability should not be assumed. Go fallback allowed. |
| OpenAI only / sensitive data | `openai-only-sensitive` | Same-provider fallbacks only. No OpenCode Go. |
| OpenCode Go only | TODO | Candidate: GLM-5.1 for long-horizon, Kimi K2.6 search, MiMo large/multimodal, MiniMax/Qwen cheap. Needs live validation. |
| GPT subscription only | TODO | Candidate: GPT-5.5/5.4 plus GPT-5.4-mini; no cross-provider fallback. |
| Cursor/Copilot/Antigravity mixed | TODO | Needs separate local auth and model-ID validation. |

## How to add a new combo

1. Run `opencode auth list` and `opencode models <provider>` locally.
2. Create a new folder under `configs/<profile-name>/`.
3. Copy only sanitized JSON templates.
4. Run `python3 scripts/validate_configs.py configs/<profile-name>`.
5. Smoke test the main and small model.
6. Document assumptions and fallbacks in this file.
