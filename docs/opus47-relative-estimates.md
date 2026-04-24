# Opus 4.7-relative Profile Estimates

Last reviewed: 2026-04-24.

This page gives rough, decision-oriented percentage ranges for every shipped profile compared with a **pure Claude Opus 4.7** setup. It is meant to help choose a subscription/API combination; it is **not** a benchmark leaderboard.

## Baselines

`100%` means pure Opus 4.7 for that dimension.

| Baseline | What it represents | Why it matters |
| --- | --- | --- |
| Opus 4.7 Max 5x | Claude Max 5x subscription, $100/month, including Claude Code access. | Practical premium subscription baseline for frequent single-provider Claude users. |
| Opus 4.7 Max 20x | Claude Max 20x subscription, $200/month, including Claude Code access. | Heavy-use subscription baseline where capacity matters more than entry price. |
| Opus 4.7 API, cache-adjusted | Anthropic API pricing using Opus 4.7 input/output/cache-read rates. | Token-equivalent cost baseline for replacing broad Go-style workloads with Opus API calls. |

## How to read the percentages

- **Quality**: expected task success, coding/review reliability, and final-answer quality versus pure Opus 4.7.
- **Speed**: expected iteration speed/latency. `>100%` means the profile may feel faster by using mini, flash, Qwen, MiniMax, or router-auto lanes.
- **Context/specialization**: usefulness on context-heavy, multimodal, cheap-sweep, or provider-specific lanes. `>100%` is allowed when a profile is more specialized than pure Opus for that workload.
- **Resilience**: provider-diverse fallback value. Same-provider profiles are lower than cross-provider profiles because one outage/quota wall can stop more work.
- **CP/value vs Max 5x / Max 20x**: practical value-per-dollar estimate versus pure Opus subscription baselines. These assume the named non-Opus subscriptions are already part of the user's stack where noted.
- **Confidence**: confidence in the estimate, not confidence in model quality. Without a local benchmark harness, avoid treating any range as precise.

## Capability matrix

| Profile | Quality vs Opus 4.7 | Speed vs Opus 4.7 | Context/specialization vs Opus 4.7 | Resilience vs Opus 4.7 | Confidence | Main caveat |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `daily-gpt55-go-provider-diverse` | 90-105% | 105-140% | 110-160% | 130-170% | Medium | Best when GPT subscription is already available and Go is used for specialist lanes, not as universal replacement. |
| `gpt55-oauth-openai-only` | 85-100% | 100-130% | 80-110% | 70-90% | Medium | Same-provider OpenAI profile; no Go context/cheap/fallback lanes. |
| `provider-diverse-safe-gpt54-go` | 85-100% | 100-135% | 105-155% | 130-170% | Medium | OpenAI API spend must be controlled; otherwise CP drops quickly. |
| `go-first-openai-api-review` | 75-90% | 105-150% | 110-165% | 130-170% | Medium | Strong CP if OpenAI is escalation-only; weaker if Go models are asked to be final authority for hard code. |
| `openai-only-sensitive` | 80-95% | 95-120% | 75-105% | 70-90% | Medium | Good provider-boundary story, but no cross-provider outage fallback. |
| `openai-api-budget-mini` | 65-80% | 120-170% | 65-95% | 70-90% | Medium | Good for low-risk work; do not use mini-first output as final authority for complex changes. |
| `opencode-go-only-balanced` | 70-85% | 105-145% | 100-140% | 90-110% | Medium | Best low-cost single-provider-family default; quality below Opus for hard final review. |
| `opencode-go-only-low-cost` | 55-70% | 130-200% | 80-120% | 90-110% | Medium | Excellent for sweeps/classification; not a hard-debug or final-review profile. |
| `opencode-go-only-large-context` | 65-80% | 95-130% | 130-220% | 90-110% | Medium | Only beats Opus on value when the job is actually context-bound. |
| `opencode-go-only-multimodal` | 60-78% | 95-135% | 120-200% | 90-110% | Medium-low | Use for media/document-heavy work; ordinary coding should use balanced Go or GPT profiles. |
| `google-gemini-only` | 75-90% | 100-140% | 95-135% | 70-90% | Medium-low | Plan/router availability and model IDs must be verified locally. |
| `google-gemini-go-provider-diverse` | 80-95% | 105-150% | 115-170% | 130-170% | Medium-low | Good if Gemini is already available; cross-provider prompts need privacy acceptance. |
| `cursor-local-router-only` | 75-95% | 100-140% | 85-120% | 70-95% | Medium-low | Depends heavily on the local Cursor router and its current model list. |
| `cursor-go-provider-diverse` | 80-98% | 105-155% | 115-175% | 130-175% | Medium-low | Strong if Cursor is already paid and Go is used for side lanes; still needs local router smoke tests. |

## CP/value matrix against pure Opus subscriptions

These are value ranges, not literal dollar savings. They combine expected capability, capacity, and price posture. `>100%` means better practical value than the pure Opus subscription baseline for the intended workload.

| Profile | CP/value vs Opus Max 5x | CP/value vs Opus Max 20x | Best-value condition | Confidence |
| --- | ---: | ---: | --- | --- |
| `daily-gpt55-go-provider-diverse` | 250-400% | 150-260% | GPT subscription is already paid; Go handles cheap/context/specialist lanes. | Medium |
| `gpt55-oauth-openai-only` | 130-220% | 70-130% | GPT subscription is already paid and provider diversity is not needed. | Medium |
| `provider-diverse-safe-gpt54-go` | 180-320% | 100-200% | OpenAI API usage is limited to high-value lanes and Go absorbs broad work. | Medium |
| `go-first-openai-api-review` | 260-450% | 150-300% | OpenAI API is used mostly for escalation/final review. | Medium |
| `openai-only-sensitive` | 80-140% | 45-90% | Same-provider OpenAI boundary is more valuable than CP/fallback. | Medium |
| `openai-api-budget-mini` | 160-300% | 90-180% | Workload is low-risk and mini-first is acceptable. | Medium |
| `opencode-go-only-balanced` | 300-600% | 180-350% | Broad non-sensitive work where Opus-level final quality is not required every step. | Medium |
| `opencode-go-only-low-cost` | 500-900% | 250-500% | Bulk sweeps, summaries, classification, or exploration. | Medium |
| `opencode-go-only-large-context` | 250-650% | 150-380% | Large repo/log/document context is the binding constraint. | Medium |
| `opencode-go-only-multimodal` | 220-550% | 130-320% | Image/audio/video/PDF context is central to the job. | Medium-low |
| `google-gemini-only` | 120-240% | 70-140% | Gemini access is already paid/available and same-provider Google is acceptable. | Medium-low |
| `google-gemini-go-provider-diverse` | 220-450% | 130-270% | Gemini is the reasoning lane and Go handles context/cheap/multimodal work. | Medium-low |
| `cursor-local-router-only` | 120-240% | 70-140% | Cursor subscription/router is already paid and available. | Medium-low |
| `cursor-go-provider-diverse` | 220-480% | 130-290% | Cursor is the core coding lane and Go handles cheap/context side lanes. | Medium-low |

## Opus API token-equivalent check for Go-heavy workloads

OpenCode Go publishes request estimates and average token-shape assumptions for each Go model. OpenCode Go is $5 for the first month and $10/month afterward; the percentage column below uses the steady-state $10/month price. If those same broad request patterns were replaced by Opus 4.7 API calls, the rough Opus API cost can be much higher than Go's subscription price.

| Go model pattern | Go-estimated requests/month | Opus API equivalent with cache reads | Opus API equivalent without cache | Go monthly price as % of cache-adjusted Opus API equivalent |
| --- | ---: | ---: | ---: | ---: |
| GLM-5.1 | 4,300 | ~$143 | ~$1,149 | ~7.0% |
| GLM-5 | 5,750 | ~$191 | ~$1,537 | ~5.2% |
| Kimi K2.6 | 5,750 | ~$212 | ~$1,635 | ~4.7% |
| Kimi K2.5 | 9,250 | ~$341 | ~$2,630 | ~2.9% |
| MiMo-V2-Pro | 6,450 | ~$184 | ~$1,374 | ~5.4% |
| MiMo-V2.5-Pro | 6,450 | ~$184 | ~$1,374 | ~5.4% |
| MiMo-V2-Omni | 10,900 | ~$420 | ~$3,363 | ~2.4% |
| MiMo-V2.5 | 10,900 | ~$420 | ~$3,363 | ~2.4% |
| Qwen3.6 Plus | 16,300 | ~$583 | ~$4,764 | ~1.7% |
| MiniMax M2.7 | 17,000 | ~$546 | ~$4,754 | ~1.8% |
| MiniMax M2.5 | 31,800 | ~$1,022 | ~$8,892 | ~1.0% |
| Qwen3.5 Plus | 50,500 | ~$1,467 | ~$12,148 | ~0.7% |

Formula used for the cache-adjusted estimate:

```text
monthly_opus_api = requests * (
  uncached_input_tokens * 5 / 1_000_000
  + cached_tokens * 0.5 / 1_000_000
  + output_tokens * 25 / 1_000_000
)
```

The no-cache column replaces cached-token pricing with standard input pricing. This is intentionally conservative for workloads that cannot reuse prompt cache.

## Practical recommendations

| Situation | Recommended profile posture | Why |
| --- | --- | --- |
| Daily mixed coding with GPT subscription and OpenCode Go | `daily-gpt55-go-provider-diverse` | Closest to Opus-level daily quality while preserving cheap/context/fallback lanes. |
| Need one approved provider boundary | `openai-only-sensitive`, `gpt55-oauth-openai-only`, `google-gemini-only`, or `cursor-local-router-only` | Provider boundary matters more than CP/fallback. |
| Only OpenCode Go is available | `opencode-go-only-balanced` | Best general-purpose Go-only compromise. |
| Massive low-risk sweeps | `opencode-go-only-low-cost` | CP is far better than pure Opus for bulk work, but final review should escalate elsewhere. |
| Huge context or media-heavy tasks | `opencode-go-only-large-context` or `opencode-go-only-multimodal` | These can beat pure Opus value on specialized lanes even if general quality is lower. |
| If Claude Max/Opus is also available | Add Opus as a premium escalation lane later, not as a docs-only change here. | Use Opus for final review, hard debugging, architecture, and high-stakes UI/UX. |

## Sources and caveats

Official/current sources used for this estimate:

- OpenCode Go documentation: pricing, beta status, model list, monthly request estimates, and token-shape assumptions: <https://opencode.ai/docs/go/>
- Anthropic API pricing: Opus 4.7 input/output/cache prices and tokenizer caveat: <https://platform.claude.com/docs/en/about-claude/pricing>
- Anthropic Max plan: Max 5x/20x pricing, usage-limit framing, and Claude Code inclusion: <https://support.claude.com/en/articles/11049741-what-is-the-max-plan>
- Anthropic Opus 4.7 release notes: coding/agentic/multimodal positioning and benchmark caveats: <https://www.anthropic.com/news/claude-opus-4-7>
- OpenAI ChatGPT pricing page: plan feature framing for GPT/Codex access; dollar amounts are intentionally not hard-coded here because the scraped public page did not expose stable plain-text prices for every tier: <https://chatgpt.com/pricing/>

Caveats:

- These ranges are heuristic estimates for profile selection, not reproducible benchmark results.
- Local routing, rate limits, region, prompt shape, cache hit rate, and provider outages can move real outcomes materially.
- Opus 4.7 remains the premium single-model quality baseline here; profiles exceed 100% only on speed, resilience, context specialization, or CP/value dimensions.
- Re-run `opencode models <provider>` and smoke tests before treating any template profile as current on another machine.
