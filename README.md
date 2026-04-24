# OpenCode Routing Playbook

Reusable, sanitized OpenCode + oh-my-openagent routing profiles for mixed model subscriptions.

Current first profile is based on this local setup:

- GPT subscription / OpenAI OAuth available locally.
- OpenCode Go subscription available (intro pricing discussed in-session: first month $5, then $10/month; verify current pricing before sharing externally).
- Daily goal: GPT handles high-reliability work; OpenCode Go handles specialist lanes where it is cheaper, faster, larger-context, multimodal, or better suited.

No real API keys or tokens belong in this repo.

## Profiles

| Profile | Use when | Main model | Small model | Provider fallback |
| --- | --- | --- | --- | --- |
| `daily-gpt55-go-provider-diverse` | This machine's daily workflow; GPT-5.5 is locally executable via OpenAI OAuth | `openai/gpt-5.5` | `openai/gpt-5.4-mini` | Yes, OpenCode Go allowed |
| `provider-diverse-safe-gpt54-go` | Portable/no-GPT-5.5 profile; still allows OpenCode Go outage fallback | `openai/gpt-5.4` | `openai/gpt-5.4-mini` | Yes, OpenCode Go allowed |
| `openai-only-sensitive` | Sensitive/proprietary/compliance-bound work where cross-provider fallback is not acceptable | `openai/gpt-5.4` | `openai/gpt-5.4-mini` | No, OpenAI only |

## Quick install

Preview a profile first:

```bash
python3 scripts/validate_configs.py configs/daily-gpt55-go-provider-diverse
```

Install with backup:

```bash
scripts/install_profile.sh configs/daily-gpt55-go-provider-diverse
```

Then verify locally:

```bash
opencode debug config
opencode run -m openai/gpt-5.4-mini --variant low --title routing-smoke --dangerously-skip-permissions 'Reply with exactly: OK'
```

## Routing principle

| Job type | Preferred lane |
| --- | --- |
| Core coding / architecture / hard debugging / final review | GPT high/xhigh |
| Formal UI/UX / visual quality judgement | GPT medium |
| Quick low-risk work | GPT mini or cheap Go sweep |
| Long-horizon autonomous work | GLM-5.1 |
| Agentic search / deep exploration | Kimi K2.6 |
| 1M large-context sweeps | MiMo-V2.5-Pro |
| True multimodal image/audio/video/PDF work | MiMo-V2-Omni |
| Cheap batch sweeps | MiniMax M2.7 / Qwen3.5 Plus |
| Fast UI prototype / option generation | Qwen3.6 Plus |

## Safety notes

- `fallback_models` depends on oh-my-openagent, not plain OpenCode alone.
- Cross-provider fallback can send prompt/code to a different provider. Use `openai-only-sensitive` for sensitive repos.
- Keep real secrets in environment variables or a secrets manager; do not paste raw configs with tokens into issues/PRs/AI prompts.
- Pin `@latest` dependencies before using this in production/CI.
