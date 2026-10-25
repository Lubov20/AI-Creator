from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8').replace('clamp(energy*3.5,0.,1.)','clamp(energy*2.4,0.,1.)').replace('p.xy+=f*(1.6+seed.y*1.4)','p.xy+=f*(1.0+seed.y*.7)').replace('vEnergy*.22','vEnergy*.06').replace('vec3(1.,.28,.71)*(bright+vGlint*.7)','vec3(.8,.9,.9)*(bright+vGlint*.25)');p.write_text(s,encoding='utf8')
p=Path('dist/fluid.js');s=p.read_text(encoding='utf8').replace('movement*weight*3.5','movement*weight*2.4');p.write_text(s,encoding='utf8')
