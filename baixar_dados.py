from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, zipfile
root=Path(__file__).resolve().parent/'dados'; root.mkdir(parents=True,exist_ok=True)
sources={
 'melbourne':'https://www.kaggle.com/api/v1/datasets/download/dansbecker/melbourne-housing-snapshot',
 'kpmg':'https://www.kaggle.com/api/v1/datasets/download/archit9406/customer-transaction-dataset',
 'shein':'https://www.kaggle.com/api/v1/datasets/download/oleksiimartusiuk/e-commerce-data-shein',
 'adult':'https://archive.ics.uci.edu/static/public/2/adult.zip',
 'diamonds':'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'}
def get(item):
 name,url=item; dest=root/name; dest.mkdir(exist_ok=True)
 try:
  data=urllib.request.urlopen(url,timeout=90).read()
  path=dest/('diamonds.csv' if name=='diamonds' else 'download.zip');path.write_bytes(data)
  if name!='diamonds':
   with zipfile.ZipFile(path) as z:z.extractall(dest)
  return name,[(str(p),p.stat().st_size) for p in dest.rglob('*') if p.is_file()]
 except Exception as e:return name,str(e)
for r in ThreadPoolExecutor(5).map(get,sources.items()):print(r,flush=True)
