#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

SECRET_PATTERNS = [
    re.compile(r'(?i)(api[_-]?key|api[_-]?token|authorization|password|secret)"?\s*:\s*"(?!\$\{?)[^"<][^"]{8,}"'),
    re.compile(r'sk-[A-Za-z0-9_-]{16,}'),
]


def load(path: Path):
    with path.open() as f:
        return json.load(f)


def walk_models(obj, acc):
    if isinstance(obj, dict):
        if isinstance(obj.get('model'), str):
            acc.add(obj['model'])
        for v in obj.values():
            walk_models(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            walk_models(v, acc)
    elif isinstance(obj, str) and '/' in obj and (obj.startswith('openai/') or obj.startswith('opencode-go/')):
        acc.add(obj)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    files = [root / 'opencode.json', root / 'oh-my-openagent.json']
    ok = True
    models = set()
    for path in files:
        if not path.exists():
            print(f'MISSING {path}')
            ok = False
            continue
        text = path.read_text()
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                print(f'POSSIBLE_SECRET {path}')
                ok = False
        try:
            data = json.loads(text)
        except Exception as e:
            print(f'INVALID_JSON {path}: {e}')
            ok = False
            continue
        walk_models(data, models)
    if (root / 'oh-my-openagent.json').exists():
        d = load(root / 'oh-my-openagent.json')
        missing = []
        for section in ('agents', 'categories'):
            for name, cfg in d.get(section, {}).items():
                if not cfg.get('fallback_models'):
                    missing.append(f'{section}.{name}')
        if missing:
            print('MISSING_FALLBACKS ' + ', '.join(missing))
            ok = False
    print('models=' + ', '.join(sorted(models)))
    print('OK' if ok else 'FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
