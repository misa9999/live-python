from requests import get
from shutil import copyfileobj
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


for day,file_ in zip(days, files_list):
    print(file_)
    download_file('{}.pdf'.format(day), file_)
