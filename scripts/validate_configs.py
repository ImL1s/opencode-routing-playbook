#!/usr/bin/env python3
"""Validate installable OpenCode/oh-my-openagent profile templates.

Usage:
  python3 scripts/validate_configs.py                 # validate every configs/* profile and profiles.json
  python3 scripts/validate_configs.py configs/<name>  # validate one profile directory
"""
import json
import re
import sys
from pathlib import Path
from typing import Any

SECRET_PATTERNS = [
    re.compile(r'(?i)(api[_-]?key|api[_-]?token|authorization|password|secret)"?\s*:\s*"(?!\$\{?)[^"<][^"]{8,}"'),
    re.compile(r'sk-[A-Za-z0-9_-]{16,}'),
    re.compile(r'ghp_[A-Za-z0-9_]{20,}'),
    re.compile(r'github_pat_[A-Za-z0-9_]{20,}'),
    re.compile(r'AKIA[0-9A-Z]{16}'),
    re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----'),
]
LOCAL_PATH_PATTERNS = [
    re.compile(r'/Users/[^"\s)]+'),
    re.compile(r'/private/tmp/[^"\s)]+'),
]
MODEL_PREFIXES = {
    'openai',
    'opencode-go',
    'google',
    'cursor',
    'cursor-acp',
    'ollama',
}
PLUGIN_OR_AUTH_MANAGED_PROVIDERS = {'openai', 'opencode-go'}
CUSTOM_PROVIDER_BLOCK_REQUIRED = {'google', 'cursor', 'cursor-acp', 'ollama'}


def load_json(path: Path) -> Any:
    with path.open() as f:
        return json.load(f)


def model_prefix(model: str) -> str:
    return model.split('/', 1)[0]


def model_name(model: str) -> str:
    return model.split('/', 1)[1]


def walk_models(obj: Any, acc: set[str]) -> None:
    if isinstance(obj, dict):
        if isinstance(obj.get('model'), str):
            acc.add(obj['model'])
        for v in obj.values():
            walk_models(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            walk_models(v, acc)
    elif isinstance(obj, str) and '/' in obj and obj.split('/', 1)[0] in MODEL_PREFIXES:
        acc.add(obj)


def scan_text(path: Path, text: str) -> list[str]:
    issues: list[str] = []
    for pat in SECRET_PATTERNS:
        if pat.search(text):
            issues.append(f'POSSIBLE_SECRET {path}')
            break
    for pat in LOCAL_PATH_PATTERNS:
        if pat.search(text):
            issues.append(f'LOCAL_ABSOLUTE_PATH {path}')
            break
    return issues


def repo_root_for(path: Path) -> Path | None:
    path = path.resolve()
    candidates = [path, path.parent, path.parent.parent]
    for c in candidates:
        if (c / 'profiles.json').exists() and (c / 'configs').exists():
            return c
    return None


def rel_to(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


def profile_entry_for(profile_dir: Path, repo_root: Path | None) -> dict[str, Any] | None:
    if not repo_root:
        return None
    index = repo_root / 'profiles.json'
    if not index.exists():
        return None
    data = load_json(index)
    rel = rel_to(profile_dir, repo_root)
    for p in data.get('profiles', []):
        if isinstance(p, dict) and p.get('profile_dir') == rel:
            return p
    return None


def validate_provider_boundaries(profile_dir: Path, opencode_cfg: dict[str, Any], models: set[str], messages: list[str]) -> bool:
    ok = True
    entry = profile_entry_for(profile_dir, repo_root_for(profile_dir))
    if not entry:
        return True

    allowed = set(entry.get('providers', []))
    used_prefixes = {model_prefix(m) for m in models if '/' in m}
    unknown = sorted(used_prefixes - MODEL_PREFIXES)
    if unknown:
        messages.append('UNKNOWN_MODEL_PREFIX ' + ', '.join(unknown))
        ok = False

    disallowed = sorted(used_prefixes - allowed)
    if disallowed:
        messages.append(f'MODEL_PROVIDER_NOT_ALLOWED {entry.get("name")}: ' + ', '.join(disallowed))
        ok = False

    provider_block = opencode_cfg.get('provider', {})
    if provider_block is None:
        provider_block = {}
    if not isinstance(provider_block, dict):
        messages.append('INVALID_PROVIDER_BLOCK')
        return False

    extra_provider_blocks = sorted(set(provider_block) - allowed)
    if extra_provider_blocks:
        messages.append(f'EXTRA_PROVIDER_BLOCKS {entry.get("name")}: ' + ', '.join(extra_provider_blocks))
        ok = False

    missing_custom_blocks = sorted((used_prefixes & CUSTOM_PROVIDER_BLOCK_REQUIRED) - set(provider_block))
    if missing_custom_blocks:
        messages.append(f'MISSING_PROVIDER_BLOCKS {entry.get("name")}: ' + ', '.join(missing_custom_blocks))
        ok = False

    for pfx, cfg in provider_block.items():
        if pfx in PLUGIN_OR_AUTH_MANAGED_PROVIDERS:
            continue
        declared = set((cfg.get('models') or {}).keys()) if isinstance(cfg, dict) else set()
        used_names = {model_name(m) for m in models if m.startswith(pfx + '/')}
        undefined = sorted(used_names - declared)
        if undefined:
            messages.append(f'UNDECLARED_PROVIDER_MODELS {entry.get("name")}.{pfx}: ' + ', '.join(undefined))
            ok = False
    return ok


def validate_profile(root: Path) -> tuple[bool, set[str], list[str]]:
    files = [root / 'opencode.json', root / 'oh-my-openagent.json']
    ok = True
    models: set[str] = set()
    messages: list[str] = []
    opencode_cfg: dict[str, Any] = {}

    for path in files:
        if not path.exists():
            messages.append(f'MISSING {path}')
            ok = False
            continue
        text = path.read_text()
        found = scan_text(path, text)
        if found:
            messages.extend(found)
            ok = False
        try:
            data = json.loads(text)
        except Exception as e:  # noqa: BLE001 - command-line validator should report parse exception
            messages.append(f'INVALID_JSON {path}: {e}')
            ok = False
            continue
        if path.name == 'opencode.json':
            opencode_cfg = data
        walk_models(data, models)

    for md in sorted(root.glob('*.md')):
        found = scan_text(md, md.read_text())
        if found:
            messages.extend(found)
            ok = False

    ohmy_path = root / 'oh-my-openagent.json'
    if ohmy_path.exists():
        try:
            d = load_json(ohmy_path)
        except Exception:
            d = {}
        missing = []
        for section in ('agents', 'categories'):
            section_data = d.get(section, {})
            if not isinstance(section_data, dict) or not section_data:
                messages.append(f'MISSING_SECTION {ohmy_path}:{section}')
                ok = False
                continue
            for name, cfg in section_data.items():
                if not isinstance(cfg, dict):
                    messages.append(f'INVALID_ROUTE {section}.{name}')
                    ok = False
                    continue
                if not cfg.get('model'):
                    messages.append(f'MISSING_MODEL {section}.{name}')
                    ok = False
                if not cfg.get('fallback_models'):
                    missing.append(f'{section}.{name}')
        if missing:
            messages.append('MISSING_FALLBACKS ' + ', '.join(missing))
            ok = False

    if opencode_cfg:
        ok = validate_provider_boundaries(root, opencode_cfg, models, messages) and ok

    return ok, models, messages


def profile_dirs(root: Path) -> list[Path]:
    if (root / 'opencode.json').exists() or (root / 'oh-my-openagent.json').exists():
        return [root]
    configs = root / 'configs'
    if configs.exists():
        return sorted(p for p in configs.iterdir() if p.is_dir())
    return [root]


def validate_index(root: Path, dirs: list[Path]) -> tuple[bool, list[str]]:
    index = root / 'profiles.json'
    if not index.exists():
        return True, []
    ok = True
    messages: list[str] = []
    try:
        data = load_json(index)
    except Exception as e:  # noqa: BLE001
        return False, [f'INVALID_JSON {index}: {e}']
    profiles = data.get('profiles')
    if not isinstance(profiles, list) or not profiles:
        return False, ['profiles.json has no profiles array']
    names = [p.get('name') for p in profiles if isinstance(p, dict)]
    if len(names) != len(set(names)):
        ok = False
        messages.append('DUPLICATE_PROFILE_NAMES')
    dir_set = {rel_to(p, root) for p in dirs}
    indexed_dirs = set()
    for p in profiles:
        if not isinstance(p, dict):
            ok = False
            messages.append('INVALID_PROFILE_ENTRY')
            continue
        for key in ('name', 'profile_dir', 'main_model', 'small_model', 'providers', 'recommended_for', 'verification_status'):
            if key not in p or p[key] in (None, '', []):
                ok = False
                messages.append(f'MISSING_PROFILE_FIELD {p.get("name", "<unknown>")}.{key}')
        profile_dir = p.get('profile_dir')
        if isinstance(profile_dir, str):
            indexed_dirs.add(profile_dir)
            if profile_dir not in dir_set:
                ok = False
                messages.append(f'PROFILE_DIR_NOT_FOUND {profile_dir}')
        providers = p.get('providers', [])
        if not isinstance(providers, list) or any(provider not in MODEL_PREFIXES for provider in providers):
            ok = False
            messages.append(f'INVALID_PROFILE_PROVIDERS {p.get("name", "<unknown>")}')
    unindexed = sorted(dir_set - indexed_dirs)
    if unindexed:
        ok = False
        messages.append('UNINDEXED_PROFILE_DIRS ' + ', '.join(unindexed))
    return ok, messages


def scan_repo_docs(root: Path) -> tuple[bool, list[str]]:
    ok = True
    messages: list[str] = []
    for path in [root / 'README.md', root / '.env.example', *sorted((root / 'docs').glob('*.md'))]:
        if not path.exists():
            continue
        found = scan_text(path, path.read_text())
        if found:
            ok = False
            messages.extend(found)
    return ok, messages


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    root = root.resolve()
    dirs = profile_dirs(root)
    all_ok = True
    all_models: set[str] = set()
    for d in dirs:
        ok, models, messages = validate_profile(d)
        all_ok = all_ok and ok
        all_models.update(models)
        print(f'== {d} ==')
        for m in messages:
            print(m)
        print('models=' + ', '.join(sorted(models)))
        print('OK' if ok else 'FAIL')

    if (root / 'profiles.json').exists():
        for label, fn in [('profiles.json', lambda: validate_index(root, dirs)), ('repo-docs', lambda: scan_repo_docs(root))]:
            ok, messages = fn()
            all_ok = all_ok and ok
            print(f'== {label} ==')
            for m in messages:
                print(m)
            print('OK' if ok else 'FAIL')

    print('== summary ==')
    print('profiles=' + str(len(dirs)))
    print('models=' + ', '.join(sorted(all_models)))
    print('OK' if all_ok else 'FAIL')
    return 0 if all_ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
