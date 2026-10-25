import urllib.request
from pathlib import Path
base='https://cdn.jsdelivr.net/npm/three@0.170.0/'
for src,dst in [('build/three.module.js','three.module.js'),('examples/jsm/loaders/FontLoader.js','FontLoader.js'),('examples/jsm/geometries/TextGeometry.js','TextGeometry.js'),('examples/fonts/helvetiker_bold.typeface.json','digits.json')]:
 data=urllib.request.urlopen(base+src).read();Path('dist/vendor/'+dst).write_bytes(data);print(dst,len(data))
