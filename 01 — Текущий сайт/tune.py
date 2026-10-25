from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8').replace("let world,detail,filter='all'","let hasPointer=false;\nlet world,detail,filter='all'")
s=s.replace("addEventListener('pointermove',e=>{screenPointer", "addEventListener('pointermove',e=>{hasPointer=true;screenPointer")
s=s.replace('uniforms.motion.value=reduced?0:1','uniforms.motion.value=reduced||!hasPointer?0:1')
s=s.replace('opacity:{value:1}},vertexShader:cardVertex','opacity:{value:.84}},vertexShader:cardVertex')
p.write_text(s,encoding='utf8')
