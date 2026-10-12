"""Enforce the English-content policy by rejecting Cyrillic in repository text.

This is a regression guard, not automatic language identification or translation.
Git history is not current working-tree content.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CYRILLIC = re.compile(r"[\u0400-\u04ff]")
files = subprocess.check_output(
    ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
    cwd=ROOT,
).decode("utf-8").split("\0")
errors = []
checked = 0
for name in sorted(set(files) - {""}):
    path = ROOT / name
    if not path.is_file():
        continue
    try:
        body = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    checked += 1
    for number, line in enumerate(body.splitlines(), 1):
        if CYRILLIC.search(line):
            errors.append(f"{name}:{number}: Cyrillic content violates the English-only policy")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"English-content guard passed for {checked} text files")
