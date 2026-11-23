#!/usr/bin/env python3
"""Static checks for Shader Wiki: sources, topic structure, internal paths."""
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
try: data=json.loads((ROOT/'sources.json').read_text(encoding='utf-8'))
except Exception as e:
 print('FAIL sources.json:',e); sys.exit(1)
ids=[d['id'] for d in data]
if len(data)<5: errors.append('fewer than five source documents')
if len(set(ids))!=len(ids):errors.append('duplicate source IDs')
urls=[d['url'] for d in data]
if len(set(urls))!=len(urls):errors.append('duplicate source URLs')
if len([f for f in (ROOT/'wiki/topics').glob('*.md')])!=len(data):errors.append('topic count does not match sources')
required=['## 核心概念','## 常見誤解','## 自我檢查','## 來源與可追溯性']
for d in data:
 sid=d['id'];slug=d['topic_slug']
 raw=ROOT/'raw'/f'{sid.lower()}-source-note.md'
 topic=ROOT/'wiki/topics'/f'{slug}.md'
 if not raw.exists():errors.append(f'{sid}: missing raw source note')
 if not topic.exists():errors.append(f'{sid}: missing topic file');continue
 content=topic.read_text(encoding='utf-8')
 for label in required:
  if label not in content:errors.append(f'{sid}: missing section {label}')
 for piece in [sid,d['url'],f'W{sid[1:]}']:
  if piece not in content:errors.append(f'{sid}: missing citation {piece}')
 if f'(topics/{slug}.md)' not in (ROOT/'wiki/index.md').read_text(encoding='utf-8'):
  errors.append(f'{sid}: missing index reference')
for f in ROOT.rglob('*.md'):
 content=f.read_text(encoding='utf-8')
 for match in re.finditer(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',content):
  target=match.group(1).split('#')[0]
  if not target or re.match(r'^(https?://|mailto:)',target):continue
  if not (f.parent/target).exists():errors.append(f'{f.relative_to(ROOT)}: broken relative link {target}')
print(f'Sources: {len(data)} | Wiki topics: {len(list((ROOT/"wiki/topics").glob("*.md")))}')
print(f'Result: {"PASS" if not errors else "FAIL"} ({len(errors)} errors)')
for e in errors:print(' -',e)
sys.exit(bool(errors))
