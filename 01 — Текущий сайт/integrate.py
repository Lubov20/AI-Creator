from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8').replace('const spine=createSpine();','const spine=await createSpine();')
s=s.replace('w.spine.rotation.y=t*.035;','w.spine.rotation.y=Math.sin(t*.12)*.065+(screenPointer.x-.5)*.09;')
s=s.replace("const camera=new THREE.PerspectiveCamera(39,1,.1,80);", "const camera=new THREE.PerspectiveCamera(39,1,.1,80);const cosmos=createGlitter(r);scene.add(cosmos);")
s=s.replace('detail={host,r,effect,scene,camera,root,u};','detail={host,r,effect,scene,camera,root,u,cosmos};')
s=s.replace('detail.u.flow.value=detail.effect.step(dt,reduced);', 'detail.u.flow.value=detail.effect.step(dt,reduced);detail.cosmos.material.uniforms.flow.value=detail.u.flow.value;detail.cosmos.material.uniforms.time.value=t;detail.cosmos.material.uniforms.pointer.value.copy(screenPointer);detail.cosmos.material.uniforms.aspect.value=innerWidth/innerHeight;detail.cosmos.material.uniforms.motion.value=reduced||!hasPointer?0:1;')
p.write_text(s,encoding='utf8')
