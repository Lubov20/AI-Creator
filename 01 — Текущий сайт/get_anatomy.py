import urllib.request,csv,io
u='https://raw.githubusercontent.com/olivercase/body_parts_3d_api/main/MANIFEST.csv'
s=urllib.request.urlopen(u,timeout=30).read().decode();rows=list(csv.DictReader(io.StringIO(s)));print('fields',rows[0].keys())
for r in rows:
 if any(w in str(r).lower() for w in ['lumbar vertebra','thoracic vertebra','cervical vertebra']):print(r)
