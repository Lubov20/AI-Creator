from pathlib import Path
p=Path('dist/fluid.js');s=p.read_text(encoding='utf8').replace('vec3(.12,.17,.17)*(film-.4)','vec3(.018,.027,.025)*(film-.4)').replace('*.013;col*=','*.0007;col*=');p.write_text(s,encoding='utf8')
p=Path('dist/app.js');s=p.read_text(encoding='utf8').replace('lerp(2.05,1.35','lerp(1.1,.75').replace('lerp(1.35,8,rise)','lerp(.75,8,rise)').replace('opacity:.65});const vertebrae','opacity:.45});const vertebrae')
s=s.replace("function currentIndex(){return Math.round(clamp((phase-.25)/.52)*5)}", "function currentIndex(){const value=clamp((phase-.25)/.52)*5;return projects.filter(p=>filter==='all'||p.type===filter).reduce((a,b)=>Math.abs(a.index-value)<Math.abs(b.index-value)?a:b).index}")
s=s.replace("b.onclick=()=>{$('#contact').showModal();", "b.onclick=()=>{if(projectDialog.open)finishClose();$('#contact').showModal();")
p.write_text(s,encoding='utf8')
p=Path('dist/index.html');s=p.read_text(encoding='utf8').replace('<span class="scroll-close">','<div class="detail-navigation"><nav aria-label="Навигация проекта"><button data-go="work">Работы</button><i></i><button data-go="academy">Академия</button><i></i><button data-contact>Контакт</button></nav></div><span class="scroll-close">');p.write_text(s,encoding='utf8')
p=Path('dist/style.css');s=p.read_text(encoding='utf8')+'\n.detail-navigation{position:absolute;top:5.5%;right:3.5%;z-index:5}@media(max-width:600px){.detail-navigation{top:24px;right:5%;left:5%;display:flex;justify-content:flex-end}}';p.write_text(s,encoding='utf8')
