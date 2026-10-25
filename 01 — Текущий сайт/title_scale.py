from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8').replace("ctx.font='38px monospace'","ctx.font='64px monospace'").replace("ctx.fillText('РАБОТА',512,322)","ctx.fillText('РАБОТА',512,308)").replace("padStart(2,'0'),512,372)","padStart(2,'0'),512,388)");p.write_text(s,encoding='utf8')
