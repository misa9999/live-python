from collections import namedtuple
from pprint import pprint
from bs4 import BeautifulSoup as bs
from requests import get


def get_last_page(url: str) -> str:
	pyjobs = get(url)
	pyjobs_page = bs(pyjobs.text, 'html.parser')
	links = pyjobs_page.find('ul', {'class':'pagination'}).find_all('a')
	return max([link.get('href') for link in links])


def trata_strs1(string: str) -> str:
    """Remove os rótulos de descrição das caixas."""
    return string.split(':')[1].strip()



def trata_strs2(string: str) -> str:
    """Remove os rótulos de descrição das caixas."""
    return string.split('\n')[1].strip()


def gen_jobs(url: str) -> namedtuple:
    num = 1
    pyjobs = get(url)
    pyjobs_page = bs(pyjobs.text, 'html.parser')
    boxes = pyjobs_page.find_all('div', {'class':'col-md-8'})

    for box in boxes:
        titulo = box.find('h2').text
        ps = box.find_all('p')
        tipo =  ps[0].text                                                                                                                                                                
        empresa = ps[1].text
        nivel =   ps[2].text
        local = ps[3].text
        
        yield vaga(titulo, tipo, 
                   trata_strs1(empresa), 
                   trata_strs2(nivel), 
                   trata_strs2(local))
        print('----'*30)


vaga = namedtuple('Vaga', 'Titulo tipo empresa nivel local')
base_url = 'https://www.pyjobs.com.br/'
jobs = f'{base_url}jobs/'
job_pages = f'{jobs}?page='


last_page = int(get_last_page(jobs)[-1])
urls = [f'{job_pages}{n}' for n in range(1, last_page+1)]

for url in urls:
    pprint(list(gen_jobs(url)))

    