from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8').replace('group.position.x=1.1;scene.add(group)','group.position.set(1.1,0,-3.6);scene.add(group)').replace('Math.cos(a)*4.7-3.6','Math.cos(a)*4.7')
s=s.replace('reduce?1:smooth((p-.015)/.10)','reduce||gal.manual!==0?1:smooth((p-.015)/.10)')
s=s.replace("$('.gallery-caption').style.opacity=reveal;", "$('.gallery-caption').style.opacity=reveal;$('.gallery-caption').inert=reveal<.1;")
s=s.replace('gal.target-=delta*Math.PI*2/6;updateCaption','gal.target-=delta*Math.PI*2/6;scrollDirty=true;updateCaption')
s=s.replace("window.scrollTo({top:0,behavior:reduce?'instant':'smooth'})", "window.scrollTo({top:a.getAttribute('href')==='#work'?($('.universe').offsetHeight-innerHeight)*.14:0,behavior:reduce?'instant':'smooth'})")
p.write_text(s,encoding='utf8')
