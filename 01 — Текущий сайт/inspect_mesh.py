from pathlib import Path
import urllib.request
Path('dist/vendor/BufferGeometryUtils.js').write_bytes(urllib.request.urlopen('https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/utils/BufferGeometryUtils.js',timeout=30).read())
for p in sorted(Path('dist/assets/anatomy').glob('*.obj')):
 v=[[float(t) for t in line.split()[1:4]] for line in p.read_text().splitlines() if line.startswith('v ')]
 print(p.name,[(round(min(x[k] for x in v),2),round(max(x[k] for x in v),2)) for k in range(3)])
