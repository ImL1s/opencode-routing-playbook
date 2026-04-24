# Session Summary

This repo captures the model-routing decision process from the GPT + OpenCode Go setup session.

## Final decision

Use a profile system rather than a single universal config:

1. **Daily local profile**: GPT-5.5-first because this machine has OpenAI OAuth and `opencode run -m openai/gpt-5.5` smoke-tested successfully.
2. **Provider-diverse safe profile**: GPT-5.4-first for environments where GPT-5.5 API availability should not be assumed, while still keeping OpenCode Go fallback lanes.
3. **OpenAI-only sensitive profile**: same-provider fallbacks only; use when code/data should not cross provider boundaries.

## Important corrections made during review

- `openai/gpt-5.4-mini-fast` was replaced with the standard model ID `openai/gpt-5.4-mini` in shareable configs.
- API-safe/provider-diverse `openai-codex` gained fallback coverage.
- `multimodal-looker` was changed to MiMo-V2-Omni primary because its name means real multimodal input.
- A dedicated `ui-prototype` category was added using Qwen3.6 Plus; formal UI/UX remains GPT-led.
- Config file permissions on the local machine were tightened to `600` after security review.

## Team-review takeaways

- Strategy is coherent: GPT for reliability; Go for specialist lanes.
- Do not assume GPT-5.5 API-key availability everywhere; keep GPT-5.4 profile for portability.
- `fallback_models` is an oh-my-openagent feature; plain OpenCode may not honor these chains.
- Cross-provider fallbacks are operationally useful but can be a privacy boundary risk.
- Keep OpenAI-only profile for sensitive work.
