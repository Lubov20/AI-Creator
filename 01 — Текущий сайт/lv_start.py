from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8')
s=s.replace("import * as THREE from 'three';", "import * as THREE from 'three';\nimport {FontLoader} from './vendor/FontLoader.js';\nimport {TextGeometry} from './vendor/TextGeometry.js';")
s=s.replace('uniform float time,velocity,hover;varying vec2 vUv;void main(){vec2 p=', 'uniform float time,velocity,hover,reveal;varying vec2 vUv;void main(){vec2 p=')
s=s.replace('gl_FragColor=vec4(col,edge);','gl_FragColor=vec4(col,edge*reveal);')
s=s.replace('function initGallery(){','async function initGallery(){')
s=s.replace('hover:{value:0}},vertexShader:cardVertex','hover:{value:0},reveal:{value:0}},vertexShader:cardVertex')
old='gal={host,r,scene,camera,group,cards,helix,rings,angle:0,target:0,manual:0,index:0,progress:0};'
new='''const font=new FontLoader().parse(await(await fetch('./vendor/digits.json')).json());const letterGeo=new TextGeometry('LV',{font,size:1.45,depth:.28,curveSegments:10,bevelEnabled:true,bevelThickness:.045,bevelSize:.035,bevelSegments:3});letterGeo.center();const monogram=new THREE.Group();const letterMat=new THREE.MeshPhysicalMaterial({color:'#e3b6d6',metalness:.35,roughness:.2,iridescence:.9,clearcoat:1,transparent:true});const letters=new THREE.Mesh(letterGeo,letterMat);monogram.add(letters);let emblemRing=new THREE.Mesh(new THREE.TorusGeometry(1.65,.018,8,160),new THREE.MeshStandardMaterial({color:'#d19abd',metalness:.3,roughness:.22,transparent:true}));monogram.add(emblemRing);monogram.position.set(innerWidth<600?0:1.5,.05,.4);scene.add(monogram);scene.add(new THREE.HemisphereLight('#d7e9ea','#2c1936',2.5));let key=new THREE.DirectionalLight('#f5e8ff',5);key.position.set(-3,5,6);scene.add(key);let light=new THREE.PointLight('#ff71c5',60,20);light.position.set(5,-1,3);scene.add(light);gal={host,r,scene,camera,group,cards,helix,rings,monogram,letterMat,emblemRing,angle:0,target:0,manual:0,index:0,progress:0};'''
s=s.replace(old,new)
s=s.replace('try{initGallery();document.body','try{await initGallery();document.body')
s=s.replace("gal.progress=p;gal.target=", "gal.progress=p;const reveal=reduce?1:smooth((p-.015)/.10);gal.cards.forEach(c=>c.material.uniforms.reveal.value=reveal);gal.monogram.visible=reveal<.99;gal.letterMat.opacity=1-reveal;gal.emblemRing.material.opacity=1-reveal;$('.gallery-caption').style.opacity=reveal;gal.target=")
s=s.replace('gal.group.rotation.y=gal.angle;', 'gal.group.rotation.y=gal.angle;gal.monogram.rotation.y=Math.sin(t*.25)*.35;gal.monogram.rotation.z=Math.sin(t*.18)*.06;gal.monogram.position.y=Math.sin(t*.4)*.12;')
p.write_text(s,encoding='utf8')
