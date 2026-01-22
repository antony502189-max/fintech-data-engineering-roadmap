"""Offline exercise CLI. Run from repository root; no dependencies required."""
from pathlib import Path
import argparse
import copy
import importlib.util
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

def load(path):
    spec=importlib.util.spec_from_file_location('submission',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.solve

def grade(identity,path,cases):
    solve=load(path)
    failed=0
    for n,case in enumerate(cases,1):
        argument=copy.deepcopy(case['input'])
        try:
            actual=solve(argument)
            # JSON roundtrip enforces return contract and normalizes tuple/list.
            actual=json.loads(json.dumps(actual,allow_nan=False))
            success=(json.dumps(actual,sort_keys=True)==json.dumps(case['expected'],sort_keys=True)
                     and argument==case['input'])
            if not success:
                print(f'{identity} case {n}: expected {case["expected"]!r}, got {actual!r}; input unchanged={argument==case["input"]}')
        except Exception as exc:
            success=False
            print(f'{identity} case {n}: {type(exc).__name__}: {exc}')
        failed+=not success
    print(f'{identity}: {len(cases)-failed}/{len(cases)} passed')
    return failed

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['init','grade','reference','verify'])
    parser.add_argument('exercise',nargs='?')
    parser.add_argument('--submission',type=Path)
    args=parser.parse_args()
    cases=json.loads((ROOT/'practice/cases.json').read_text(encoding='utf-8'))
    if args.action!='verify' and args.exercise not in cases:
        parser.error('Choose an exercise from E01 through E40')
    if args.action=='init':
        target=ROOT/'work/answers'/f'{args.exercise}.py'
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists(): parser.error(f'Already exists; preserved: {target}')
        target.write_text((ROOT/'practice/starters'/f'{args.exercise}.py').read_text(encoding='utf-8'),encoding='utf-8')
        print(f'Created {target}'); return
    if args.action=='verify':
        failed=sum(grade(identity,ROOT/'practice/solutions'/f'{identity}.py',sample) for identity,sample in cases.items())
    else:
        path=(ROOT/'practice/solutions'/f'{args.exercise}.py' if args.action=='reference'
              else args.submission or ROOT/'work/answers'/f'{args.exercise}.py')
        if not path.exists(): parser.error(f'Missing {path}; run init first')
        failed=grade(args.exercise,path,cases[args.exercise])
    if failed: sys.exit(1)

if __name__=='__main__': main()
