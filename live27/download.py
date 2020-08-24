from shutil import copyfileobj
from requests import get

base_url = 'http://www.dje.tjsp.jus.br/cdje/downloadCaderno.do?dtDiario=10/01/2020&cdCaderno=12&tpDownload=D'

file_ = 'teste.pdf'
xpto = get(base_url, stream=True)

with open(file_, 'wb') as f:
    copyfileobj(xpto.raw, f)