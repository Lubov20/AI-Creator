from pathlib import Path
p=Path('dist/fluid.js');s=p.read_text(encoding='utf8').replace('movement*weight*5.5','movement*weight*3.5').replace('flow*.018+c*transition*.008','flow*.006+c*transition*.006');p.write_text(s,encoding='utf8')
p=Path('dist/app.js');s=p.read_text(encoding='utf8').replace('q*(3.+seed.y*6.)+local*seed.z*2.','q*(3.+seed.y*6.)').replace('p.xy+=f*(3.+seed.y*2.);p.z+=(seed.y-.5)*q*7.+local*(.5+seed.z*3.);','p.xy+=f*(1.6+seed.y*1.4);p.x+=sin(seed.z*30.+time)*local*.12;p.y+=cos(seed.x*30.+time)*local*.12;p.z+=(seed.y-.5)*q*7.+local*(.2+seed.z*.9);').replace('*(1.+local*.8),1.,9.','*(1.+local*.4),1.,6.').replace('pow(max(0.,vEnergy-.25),3.)*1.7','pow(max(0.,vEnergy-.25),3.)*.7')
p.write_text(s,encoding='utf8')
