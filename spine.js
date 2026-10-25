import * as THREE from 'three';
import {OBJLoader} from './vendor/OBJLoader.js';
import {mergeVertices} from './vendor/BufferGeometryUtils.js';

export async function createSpine(){
 const group=new THREE.Group(),files=await(await fetch('./assets/anatomy/manifest.json')).json(),loader=new OBJLoader();
 const objects=await Promise.all(files.map(name=>loader.loadAsync('./assets/anatomy/'+encodeURIComponent(name))));
 const bones=[],discs=[];
 objects.forEach((object,i)=>{const meshes=[];object.traverse(o=>{if(o.isMesh)meshes.push(o)});let geometry=meshes[0].geometry.clone();geometry.rotateX(-Math.PI/2);geometry.deleteAttribute('normal');geometry=mergeVertices(geometry,1e-4);geometry.computeVertexNormals();geometry.center();const pos=geometry.getAttribute('position'),uv=new Float32Array(pos.count*2);for(let j=0;j<pos.count;j++){uv[j*2]=pos.getX(j)*.06;uv[j*2+1]=pos.getY(j)*.06}geometry.setAttribute('uv',new THREE.BufferAttribute(uv,2));geometry.scale(.02,.02,.02);if(files[i].includes('disk'))discs.push(geometry);else bones.push(geometry)});
 const grainData=new Uint8Array(256*256*4);for(let i=0;i<256*256;i++){const n=120+Math.floor(Math.random()*136);grainData.set([n,n,n,255],i*4)}const grain=new THREE.DataTexture(grainData,256,256,THREE.RGBAFormat);grain.wrapS=grain.wrapT=THREE.RepeatWrapping;grain.repeat.set(3,3);grain.needsUpdate=true;
 const glass=new THREE.MeshPhysicalMaterial({color:'#86969f',metalness:.91,roughness:.30,bumpMap:grain,bumpScale:.035,clearcoat:1,clearcoatRoughness:.08,iridescence:1,iridescenceIOR:1.5,iridescenceThicknessRange:[140,500],transmission:.16,thickness:.22,ior:1.48,transparent:true,opacity:.88,envMapIntensity:1.05,side:THREE.DoubleSide});
 const discMat=new THREE.MeshPhysicalMaterial({color:'#8e9cbb',metalness:.7,roughness:.18,iridescence:.9,clearcoat:1,transparent:true,opacity:.72});
 for(let i=0;i<12;i++){const y=-7-i*.64,mesh=new THREE.Mesh(bones[i%bones.length],glass);mesh.position.set(.035*Math.sin(i*.4),y,0);mesh.rotation.set(.025*Math.sin(i*.4),.04*Math.cos(i*.3),.015*Math.sin(i));group.add(mesh);const disk=new THREE.Mesh(discs[i%discs.length],discMat);disk.position.set(mesh.position.x,y-.32,.33);group.add(disk)}
 return group;
}

export function createGlitter(renderer){
 const count=innerWidth<600?4000:9000,position=new Float32Array(count*3),colors=new Float32Array(count*3),sizes=new Float32Array(count),seeds=new Float32Array(count),far=new Float32Array(count),color=new THREE.Color();
 for(let i=0;i<count;i++){const y=-30+Math.random()*39,background=i<count*.045;let x,z;if(background){x=(Math.random()-.5)*16;z=-7+Math.random()*11}else{let a=y*1.5+Math.random()*5,rad=.45+Math.pow(Math.random(),2.2)*1.9;x=Math.cos(a)*rad;z=Math.sin(a)*rad}
 position.set([x,y,z],i*3);const h=Math.random();color.setHSL(h<.4?.48+Math.random()*.05:h<.78?.72+Math.random()*.09:.88+Math.random()*.035,.25+Math.random()*.4,.29+Math.random()*.3);colors.set([color.r,color.g,color.b],i*3);sizes[i]=.65+Math.random()*1.7;seeds[i]=Math.random();far[i]=background?1:0}
 const geometry=new THREE.BufferGeometry();geometry.setAttribute('position',new THREE.BufferAttribute(position,3));geometry.setAttribute('color',new THREE.BufferAttribute(colors,3));geometry.setAttribute('size',new THREE.BufferAttribute(sizes,1));geometry.setAttribute('seed',new THREE.BufferAttribute(seeds,1));geometry.setAttribute('farLayer',new THREE.BufferAttribute(far,1));
 const uniforms={time:{value:0},reveal:{value:0},pixel:{value:renderer.getPixelRatio()},flow:{value:null},pointer:{value:new THREE.Vector2(.5,.5)},aspect:{value:1},motion:{value:0},opacity:{value:1}};
 const material=new THREE.ShaderMaterial({uniforms,transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
 vertexShader:'uniform float time,reveal,pixel,aspect,motion,opacity;uniform sampler2D flow;uniform vec2 pointer;attribute vec3 color;attribute float size,seed,farLayer;varying vec3 vColor;varying float vAlpha,vGlint;void main(){vColor=color;vec3 p=position;p.x+=sin(time*.12+p.y+seed*6.)*.025;p.z+=cos(time*.11+p.y)*.02;vec4 mv=modelViewMatrix*vec4(p,1.);vec4 clip=projectionMatrix*mv;vec2 screen=clip.xy/clip.w*.5+.5;vec2 d=(screen-pointer)*vec2(aspect,1.);vec2 direction=normalize(d+vec2(.0001));float repel=(1.-smoothstep(.015,.12,length(d)))*.055*motion;vec2 wake=(texture2D(flow,clamp(screen,.001,.999)).rg*2.-1.)*.07;clip.xy+=(direction/vec2(aspect,1.)*repel+wake)*clip.w*2.;gl_Position=clip;float flip=.5+.5*sin(time*(.2+seed*.5)+seed*80.);vGlint=pow(flip,24.)*step(.94,seed);gl_PointSize=clamp(size*pixel*15./max(2.,-mv.z)*(1.+vGlint*.6),.7,5.5);float density=position.y< -2.?mix(reveal,.3,farLayer):.22;vAlpha=density*(.27+.30*flip+vGlint*.2)*opacity;}',
 fragmentShader:'varying vec3 vColor;varying float vAlpha,vGlint;void main(){vec2 p=gl_PointCoord-.5;float hex=max(abs(p.x)*.866+abs(p.y)*.5,abs(p.y));if(hex>.47)discard;float face=1.-smoothstep(.30,.47,hex);vec3 c=vColor*(1.+vGlint*.6);gl_FragColor=vec4(c,face*vAlpha);\n#include <colorspace_fragment>\n}'});
 const cloud=new THREE.Points(geometry,material);cloud.frustumCulled=false;return cloud;
}
