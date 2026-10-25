from pathlib import Path
p=Path('dist/fluid.js');s=p.read_text(encoding='utf8').replace('new THREE.WebGLRenderTarget(256,160,opts)','new THREE.WebGLRenderTarget(256,160,{...opts,type:THREE.HalfFloatType})')
a=s.index(' const old=renderer.getClearColor');b=s.index('\n }',a)
s=s[:a]+''' const neutral=new THREE.Scene(),neutralMaterial=new THREE.ShaderMaterial({vertexShader:vertex,fragmentShader:'void main(){gl_FragColor=vec4(.5,.5,0.,1.);}'});const neutralMesh=new THREE.Mesh(new THREE.PlaneGeometry(2,2),neutralMaterial);neutral.add(neutralMesh);renderer.setRenderTarget(this.a);renderer.render(neutral,this.camera);renderer.setRenderTarget(this.b);renderer.render(neutral,this.camera);renderer.setRenderTarget(null);neutralMesh.geometry.dispose();neutralMaterial.dispose();'''+s[b:]
p.write_text(s,encoding='utf8')
