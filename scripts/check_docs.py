"""Check local Markdown paths, lesson structure, curriculum and SQL exercise pairs."""
from pathlib import Path
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
errors=[]
files=[p for p in ROOT.rglob('*.md') if '.git' not in p.parts and 'work' not in p.relative_to(ROOT).parts]
for file in files:
    body=file.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)',body):
        if target.startswith(('https://','http://','mailto:','#')):
            continue
        path=target.split('#')[0]
        if path and not (file.parent/path).exists():
            errors.append(f'{file.relative_to(ROOT)}: missing {target}')
    if 'roadmap' in file.relative_to(ROOT).parts and file.name != 'README.md':
        sections=re.findall(r'^## (.+)$',body,re.M)
        if len(sections)!=10: errors.append(f'{file}: expected 10 lesson sections')
        if len(body.split()) < 180: errors.append(f'{file}: lesson too short')
manifest=json.loads((ROOT/'curriculum.json').read_text(encoding='utf-8'))
if [r['id'] for r in manifest] != list(range(1,101)): errors.append('Curriculum IDs must be 1..100')
if len({r['path'] for r in manifest})!=100: errors.append('Duplicate lesson paths')
for record in manifest:
    if not (ROOT/record['path']).exists(): errors.append(f"Missing {record['path']}")
for query in (ROOT/'sql/exercises').glob('*.sql'):
    if not (ROOT/'sql/solutions'/query.name).exists(): errors.append(f'Missing solution {query.name}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'Checked {len(files)} Markdown files, 100 lessons, and SQL solution pairs')
