from pathlib import Path
p=Path('dist/app.js');s=p.read_text(encoding='utf8').replace('scrollToPhase(.25+next.index/5*.52)','scrollToPhase(.28+next.index/5*.48)');p.write_text(s,encoding='utf8')
