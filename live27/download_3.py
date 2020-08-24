from multiprocessing.dummy import Pool
from shutil import copyfileobj

from requests import get
from uteis import days

days = list(map(lambda day: str(day) if len(str(day)) > 1 else '0' + str(day),
                days))

base_url = 'http://www.dje.tjsp.jus.br/cdje/downloadCaderno.do?'
full_url = '{}dtDiario=DAY/01/2020&cdCaderno=12&tpDownload=D'.format(base_url)

files_list = [full_url.replace('DAY', day) for day in days]

def download_file(name, url):
    xpto = get(base_url, stream=True)
    with open(name, 'wb') as f:
        copyfileobj(xpto.raw, f)

nodes = Pool(4)

xpto = node.map_async(lambda x: download_file('{}.pdf'.format(x[0]), x[1]),
                      zip(days, files_list))

xpto.wait()