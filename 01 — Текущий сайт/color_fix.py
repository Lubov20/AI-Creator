from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8').replace('col+=vec3(.22,.27,.25)*border*.5;','col=pow(max(col,vec3(0.)),vec3(2.2));col+=vec3(.22,.27,.25)*border*.5;')
s=s.replace('vec3 c=texture2D(image,vUv).rgb;float lum=', 'vec3 c=pow(texture2D(image,vUv).rgb,vec3(2.2));float lum=')
s=s.replace('float cut=smoothstep(.035,.18,energy);float global=', 'c=pow(max(c,vec3(0.)),vec3(2.2));float cut=smoothstep(.035,.18,energy);float global=')
p.write_text(s,encoding='utf8')
p=Path('dist/style.css');s=p.read_text(encoding='utf8')+'\n.model-credit{font-size:7px!important;margin-top:35px!important;color:#6e817b!important}.model-credit a{color:inherit;text-decoration:none}';p.write_text(s,encoding='utf8')
