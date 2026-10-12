"""Scenario-lab CLI. Execute trusted personal Python solutions, not production jobs."""
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from practice.run import grade

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['list', 'init', 'grade', 'reference', 'verify'])
    parser.add_argument('challenge', nargs='?')
    parser.add_argument('--submission', type=Path)
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'challenges/cases.json').read_text(encoding='utf-8'))
    if args.action == 'list':
        for identity, item in manifest.items():
            print(f'{identity}: {item["title"]} ({len(item["cases"])} scenarios)')
        return
    if args.action == 'verify':
        failed = sum(grade(identity, ROOT / 'challenges/solutions' / f'{identity}.py', item['cases'])
                     for identity, item in manifest.items())
    else:
        if args.challenge not in manifest:
            parser.error('Choose a challenge listed by the list command')
        identity = args.challenge
        if args.action == 'init':
            target = ROOT / 'work/challenges' / f'{identity}.py'
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                with target.open('x', encoding='utf-8', newline='\n') as handle:
                    handle.write((ROOT / 'challenges/starters' / f'{identity}.py').read_text(encoding='utf-8'))
            except FileExistsError:
                parser.error(f'Existing answer preserved: {target}')
            print(f'Created {target}')
            return
        path = (ROOT / 'challenges/solutions' / f'{identity}.py' if args.action == 'reference'
                else args.submission or ROOT / 'work/challenges' / f'{identity}.py')
        if not path.is_file():
            parser.error(f'Missing {path}; run init first')
        failed = grade(identity, path, manifest[identity]['cases'])
    if failed:
        sys.exit(1)

if __name__ == '__main__':
    main()
