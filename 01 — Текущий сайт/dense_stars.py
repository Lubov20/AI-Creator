from pathlib import Path
p=Path('dist/spine.js');s=p.read_text(encoding='utf8').replace('innerWidth<600?4200:7600','innerWidth<600?11000:22000')
s=s.replace('rank<.72?.55+Math.random()*.9:rank<.94?1.5+Math.random()*2.2:rank<.995?4+Math.random()*4.5:11+Math.random()*8','rank<.64?.7+Math.random()*1.0:rank<.93?1.9+Math.random()*2.6:rank<.995?4.8+Math.random()*5:12+Math.random()*10')
s=s.replace('white?.08:.6+Math.random()*.3','white?.08:.72+Math.random()*.26')
s=s.replace("(.10+.30*flicker):size<4.0?(.25+.48*flicker):(.08+.82*vGlint)","(.24+.48*flicker):size<4.0?(.48+.55*flicker):(.24+.95*vGlint)")
s=s.replace('vColor*(.8+vGlint*.8)','vColor*(1.1+vGlint*1.2)')
p.write_text(s,encoding='utf8')
