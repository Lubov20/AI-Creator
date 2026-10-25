import urllib.request,json
from pathlib import Path
root=Path('dist/assets/anatomy');root.mkdir(parents=True,exist_ok=True)
req=urllib.request.Request('https://api.github.com/repos/olivercase/body_parts_3d_api/git/trees/main?recursive=1',headers={'User-Agent':'LV-site-development'})
tree=json.load(urllib.request.urlopen(req,timeout=30))['tree']
ids=['FJ3154','FJ3155','FJ3156','FJ3157','FJ3159','FJ3162','FJ3212','FJ3214']
paths=[r['path'] for r in tree if any(r['path'].split('/')[-1].startswith(i+'_') for i in ids) and r['path'].endswith('.obj')]
print(paths)
for path in paths:
 name=path.split('/')[-1];data=urllib.request.urlopen('https://media.githubusercontent.com/media/olivercase/body_parts_3d_api/main/'+urllib.parse.quote(path),timeout=40).read();(root/name).write_bytes(data);print(name,len(data))
(root/'manifest.json').write_text(json.dumps([p.split('/')[-1] for p in paths]),encoding='utf8')
Path('dist/vendor/OBJLoader.js').write_bytes(urllib.request.urlopen('https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/loaders/OBJLoader.js',timeout=30).read())
