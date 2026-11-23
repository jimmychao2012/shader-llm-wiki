"""Static integrity check for Shader Wiki teaching slides. Requires only Python stdlib."""
from pathlib import Path
import re,csv,json,sys
root=Path(__file__).resolve().parents[1]
html=(root/'slides/index.html').read_text(encoding='utf-8')
slides=re.findall(r'<section class="slide(?: active)?" data-slide="(\d+)" data-wiki="([^"]+)"',html)
errors=[]
if not 8<=len(slides)<=12: errors.append(f'expected 8-12 slides; got {len(slides)}')
ids=set()
for i,(num,values) in enumerate(slides,1):
 if int(num)!=i:errors.append(f'incorrect slide number {num}')
 for w in values.split(','):
  ids.add(w)
  if w not in {f'W{i:02d}' for i in range(1,7)}:errors.append(f'invalid Wiki ID {w}')
for n in range(1,7):
 if f'W{n:02d}' not in ids: errors.append(f'missing W{n:02d}')
for target in re.findall(r'href="(\.\./wiki/topics/[^\"]+)"',html):
 if not (root/'slides'/target).resolve().is_file():errors.append(f'broken link {target}')
with (root/'workflow/slide-sources.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
sources={x['id'] for x in json.loads((root/'sources.json').read_text())}
if len(rows)!=len(slides):errors.append('slide sources row count mismatch')
for row in rows:
 for sid in row['source_ids'].split(','):
  if sid not in sources:errors.append(f'unknown source {sid}')
print(f'Wiki sources={len(sources)} slides={len(slides)} mapped wiki={len(ids)} link errors={len(errors)}')
for err in errors:print('ERROR:',err)
print('PASS' if not errors else 'FAIL')
sys.exit(1 if errors else 0)
