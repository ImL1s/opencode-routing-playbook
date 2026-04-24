# Profile Architecture

## Design goals

- **Many installable profiles, one simple installer.** Each `configs/<profile>/` is self-contained.
- **Selection by user situation.** Profiles are named by subscription/API/provider posture, not by one-off local taste.
- **No secrets.** Configs use placeholders and are safe for public GitHub.
- **Explicit provider boundaries.** Same-provider and cross-provider profiles are separated.
- **Minimal provider registration.** Profiles declare only custom provider blocks they actually use.
- **MCPs are opt-in.** Model routing profiles do not bundle BrightData/Firebase/Playwright/Mobile MCP by default.
- **Fallback chains where supported.** Every agent/category route includes `fallback_models` because these templates target oh-my-openagent.

## Provider block policy

- `openai` and `opencode-go` are treated as OpenCode/auth/plugin-managed providers; no custom `provider` block is expected in these templates.
- `google`, `cursor`, `cursor-acp`, and `ollama` require explicit provider stubs when referenced.
- A profile must not declare unrelated custom providers. For example, `openai-only-sensitive` must not contain `provider.google` or `provider.cursor-acp`.

## Naming convention

Prefer names in this shape:

```text
<provider-or-combo>-<access-or-purpose>-<routing-posture>
```

Examples:

- `daily-gpt55-go-provider-diverse`
- `openai-only-sensitive`
- `opencode-go-only-large-context`
- `cursor-go-provider-diverse`

## Profile tiers

| Tier | Meaning | Example |
| --- | --- | --- |
| Daily/local | Optimized for one known machine after smoke tests | `daily-gpt55-go-provider-diverse` |
| Portable/API-safe | Avoids assuming subscription-only model access | `provider-diverse-safe-gpt54-go` |
| Sensitive/same-provider | Avoids cross-provider prompt/code sharing | `openai-only-sensitive` |
| Cost/CP optimized | Uses cheaper models first, escalates only when needed | `go-first-openai-api-review` |
| Specialist | Built for context, multimodal, or bulk sweep constraints | `opencode-go-only-large-context` |
| Local router | Requires a local adapter/server | `cursor-local-router-only` |

## Required files per profile

- `opencode.json`: sanitized installable config with top-level `model` and `small_model`.
- `oh-my-openagent.json`: route table for `agents` and `categories`.
- `README.md`: status, fit, privacy/cost posture, install command, and smoke test.

## Validation contract

A profile should pass:

```bash
python3 scripts/validate_configs.py configs/<profile>
python3 scripts/validate_configs.py
python3 -m json.tool configs/<profile>/opencode.json >/dev/null
python3 -m json.tool configs/<profile>/oh-my-openagent.json >/dev/null
```

The validator checks JSON, profile index coverage, fallback presence, model-prefix allowlists, custom provider blocks, README/docs secret hygiene, and local absolute path leaks.
GitHub Actions runs the same validator on push and pull request.

For real adoption, also run `opencode debug config` and one `opencode run -m ...` smoke test for the main and small model.
