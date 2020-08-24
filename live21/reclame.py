from time import sleep

from bs4 import BeautifulSoup as bs
from selenium import webdriver


base_url = 'https://www.reclameaqui.com.br'
url_site = f'{base_url}/empresa/net-tv-banda-larga-e-telefone/lista-reclamacoes/'

go = webdriver.Chrome()
go.get(url_site)
# sleep(4)
bs_obj = bs(go.page_source, 'html.parser')

boxes = bs_obj.find_all('li', {'ng-repeat':'complain in vm.complainList.data track by $index | limitTo:10'})

href_links = [box.find('a').get('href') for box in boxes]
page_links = [f'{base_url}{link}' for link in href_links]

for link in page_links:
    go.get(link)
    # sleep(3)
    bs_page = bs(go.page_source, 'html.parser')
    title = bs_page.find('h1', {'class':'ng-binding'})
    recla = bs_page.find('div', {'class':'complain-body'})
    print(
        'T: {}\n\n'.format(title),
        'R: {}\n\n'.format(recla)
    )

go.quit()
