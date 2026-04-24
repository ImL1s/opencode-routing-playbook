# Session Summary

This repo started from a local GPT + OpenCode Go routing session and was then generalized into a profile catalog.

## Final decision

Use a profile system rather than a single universal config:

1. **Daily local profile**: GPT-5.5-first because this machine had OpenAI OAuth and the model smoke-tested locally.
2. **Portable API profile**: GPT-5.4-first for environments where GPT-5.5 API-key availability should not be assumed.
3. **OpenAI-only sensitive profile**: same-provider fallbacks only; use when code/data should not cross provider boundaries.
4. **Go-only and Go-first profiles**: use OpenCode Go where context, cost, multimodal support, or quota pressure makes it a better lane.
5. **Gemini/Cursor profiles**: keep provider-router setups separate so users can pick by actual subscription/API access.

## External review incorporated

Claude and Gemini both returned **BLOCK** on the first multi-profile draft. The blocking fixes were applied before commit:

- Same-provider profiles no longer carry unrelated custom provider blocks.
- Public profile `opencode.json` files no longer bundle BrightData/Firebase/Playwright/Mobile MCPs by default.
- `cursor-local-router-only` is no longer marked as cross-provider fallback just because it has both `cursor` and `cursor-acp` transports.
- README and profile READMEs now distinguish verified profiles from template profiles.
- The validator now checks provider boundaries, custom provider model declarations, profile index coverage, Markdown secret/path hygiene, and install-time validation.

## Important corrections made during review

- `openai/gpt-5.4-mini-fast` was replaced with the standard portable `openai/gpt-5.4-mini` in shareable profiles.
- API-safe/provider-diverse `openai-codex` gained fallback coverage.
- `multimodal-looker` was changed to MiMo-V2-Omni primary in Go-capable profiles because its role means real multimodal input.
- A dedicated `ui-prototype` category was added; formal UI/UX remains GPT/Gemini/Cursor-led where available.
- Local config file permissions were tightened to `600` after security review.

## Team-review takeaways

- Strategy is coherent: high-reliability models for core work; Go for specialist/CP lanes.
- Do not assume GPT-5.5 API-key availability everywhere.
- `fallback_models` is an oh-my-openagent feature; plain OpenCode may not honor these chains.
- Cross-provider fallback is an explicit privacy boundary, not just an uptime feature.
