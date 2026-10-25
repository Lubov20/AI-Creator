from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8').replace('const gallery=new THREE.Group();const cards=', 'const gallery=new THREE.Group();gallery.position.x=.55;const cards=')
s=s.replace('w.cards.forEach((c,i)=>{c.position.y=', 'w.cards.forEach((c,i)=>{c.rotation.y=i*1.13-(i*1.13+w.gallery.rotation.y)*.62;c.position.y=')
s=s.replace('col=pow(max(col,vec3(0.)),vec3(2.2));col+=', 'col=pow(max(col,vec3(0.)),vec3(2.2));float bright=max(max(col.r,col.g),col.b);col*=mix(.40,1.,smoothstep(.55,.85,bright));col+=')
p.write_text(s,encoding='utf8')
