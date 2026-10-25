from pathlib import Path
p=Path('dist/spine.js');s=p.read_text(encoding='utf8').replace('const profile=[new THREE.Vector2(.18,-.105)','const profile=[new THREE.Vector2(0,-.105),new THREE.Vector2(.18,-.105)').replace('new THREE.Vector2(.19,.105)];','new THREE.Vector2(.19,.105),new THREE.Vector2(0,.105)];');p.write_text(s,encoding='utf8')
