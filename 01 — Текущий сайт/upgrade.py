from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8')
s=s.replace("import {FlowEffect} from './fluid.js';", "import {FlowEffect} from './fluid.js';\nimport {createSpine,createGlitter} from './spine.js';\nimport {loaderReady,finishLoader} from './loader.js';")
a=s.index('function ribbon(');b=s.index('async function buildWorld()',a);s=s[:a]+s[b:]
a=s.index(' const spine=new THREE.Group();');b=s.index(' const gallery=new THREE.Group();',a)
s=s[:a]+" const spine=createSpine();scene.add(spine);const particles=createGlitter(r);scene.add(particles);\n"+s[b:]
s=s.replace("'#b96aa1'","'#ff37b1'").replace("new THREE.PointLight('#df80bf',30,30)","new THREE.PointLight('#ff39b7',45,30)")
s=s.replace('const field=w.effect.step(dt,reduced);w.cards.forEach', 'const field=w.effect.step(dt,reduced);w.particles.material.uniforms.flow.value=field;w.particles.material.uniforms.pointer.value.copy(screenPointer);w.particles.material.uniforms.aspect.value=innerWidth/innerHeight;w.particles.material.uniforms.motion.value=reduced?0:1;w.cards.forEach')
s=s.replace('try{await buildWorld()}','try{await Promise.all([buildWorld(),loaderReady])}')
s=s.replace("$('#loader').classList.add('done');targetPhase", "finishLoader();targetPhase")
s=s.replace('uniform float time,progress,opening,pixel,pointSize;attribute vec3 seed;varying vec2 vUv;varying float vAlpha,vEnergy;', 'uniform float time,progress,opening,pixel,pointSize,aspect;uniform vec2 pointer;attribute vec3 seed;varying vec2 vUv;varying float vAlpha,vEnergy,vGlint;')
s=s.replace('float local=clamp(energy*3.5,0.,1.);', 'vec2 away=(screen-pointer)*vec2(aspect,1.);float repulsion=(1.-smoothstep(.02,.15,length(away)))*smoothstep(.001,.045,energy)*.85;vec2 push=normalize(away+vec2(.0001));float local=max(clamp(energy*3.5,0.,1.),repulsion);p.xy+=push*repulsion*(.4+seed.z*.2);')
s=s.replace('vEnergy=local;vAlpha=', 'vEnergy=local;vGlint=pow(.5+.5*sin(time*1.2+seed.x*90.),20.)*local;vAlpha=')
s=s.replace('varying float vAlpha,vEnergy;void main(){vec2 q=', 'varying float vAlpha,vEnergy,vGlint;void main(){vec2 q=')
s=s.replace('c+=vec3(.75,.85,.84)*bright;', 'c=mix(c,vec3(.78,.015,.38),vEnergy*.22);c+=vec3(1.,.28,.71)*(bright+vGlint*.7);')
s=s.replace('pointSize:{value:3}};', 'pointSize:{value:3},pointer:{value:new THREE.Vector2(.5,.5)},aspect:{value:innerWidth/innerHeight}};')
s=s.replace('detail.u.time.value=t;', 'detail.u.time.value=t;detail.u.pointer.value.copy(screenPointer);detail.u.aspect.value=innerWidth/innerHeight;')
p.write_text(s,encoding='utf8')
# The loader is a canvas-based dot/contour reveal, matching the newly supplied recording.
p=Path('dist/style.css');s=p.read_text(encoding='utf8')+'''\n#loader{display:block;background:#030607}#loader canvas{position:absolute;inset:0;width:100%;height:100%;display:block}nav button.active{color:#ff9ed9}button:hover{color:#ff8bd3}.categories button[aria-pressed=true]{color:#fc8ad0}\n''';p.write_text(s,encoding='utf8')
