from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8')
s=s.replace("x.restore();let vign=", "x.restore();x.save();x.globalCompositeOperation='screen';let glow=x.createRadialGradient(570,340,10,570,340,470);glow.addColorStop(0,p.palette[1]+'55');glow.addColorStop(.5,p.palette[2]+'18');glow.addColorStop(1,'#0000');x.fillStyle=glow;x.fillRect(0,0,1024,768);x.restore();let vign=")
s=s.replace("c+=vec3(.18,.01,.1)*progress;gl_FragColor=vec4(c,vAlpha);", "float lum=max(max(c.r,c.g),c.b);float alpha=vAlpha*mix(1.,smoothstep(.012,.12,lum),smoothstep(.05,.4,progress));c+=vec3(.035,.0,.02)*progress;gl_FragColor=vec4(c,alpha);")
s=s.replace("detail={r,scene,camera,points,uniforms};", """const surface=new THREE.Mesh(new THREE.PlaneGeometry(6,4.5,70,50),new THREE.ShaderMaterial({uniforms,transparent:true,depthWrite:false,vertexShader:`uniform float progress,time;varying vec2 vUv;void main(){vUv=uv;vec3 p=position;p.z+=sin(uv.y*14.+time*.5)*progress*.5;p.x+=sin(uv.y*6.+progress*6.)*progress*.9;gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.);}`,fragmentShader:`uniform sampler2D image;uniform float progress;varying vec2 vUv;void main(){vec2 q=abs(vUv-.5)-vec2(.47,.46);float sdf=length(max(q,0.))+min(max(q.x,q.y),0.)-.025;if(sdf>0.)discard;vec3 c=texture2D(image,vUv).rgb;gl_FragColor=vec4(c,1.-smoothstep(.02,.22,progress));
+#include <colorspace_fragment>
+}`}));surface.renderOrder=2;scene.add(surface);detail={r,scene,camera,points,surface,uniforms};""".replace('\n+','\n'))
s=s.replace('detail.uniforms.pointSize.value=rect.width/180','detail.uniforms.pointSize.value=rect.height/(2*Math.tan(THREE.MathUtils.degToRad(21)))*6/detail.camera.position.z/180*1.18')
s=s.replace('detail.points.rotation.y=detailProgress*.25;','detail.points.rotation.y=detailProgress*.25;detail.surface.rotation.y=detailProgress*.25;')
p.write_text(s,encoding='utf8')
