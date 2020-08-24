from collections import namedtuple
from requests import get
from bs4 import BeautifulSoup as bs

ep_structure = namedtuple('EP', 'temporada episodio nome publicação sinopse')
url = 'https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Sword_Art_Online'

request = get(url)
page = bs(request.content, 'lxml')
tables = page.findAll('table', {'class':'wikitable'})

t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12 = tables


def get_rows(table):
    return table.findAll('tr')
    

t1_rows, t2_rows, t3_rows = map(get_rows, [t1, t2, t3])
t4_rows, t5_rows, t6_rows = map(get_rows, [t4, t5, t6])
t7_rows, t8_rows, t9_rows = map(get_rows, [t7, t8, t9])
t10_rows, t11_rows, t12_rows = map(get_rows, [t10, t11, t12])



def get_data(temp: int, rows: list) -> namedtuple:
    for row in rows:
        columns = row.find_all('td')
        ep = columns[0].text
        name = columns[1].text
        publised = [2].text
        descr = [3].text
        yield ep_structure(temp, int(ep), name, publised, descr)


t1_data, t2_data, t3_data = map(lambda t: list(get_data(t[0], t[1])), \
    enumerate([t1_rows, t2_rows, t3_rows]))

t4_data, t5_data, t6_data = map(lambda t: list(get_data(t[0], t[1])), \
    enumerate([t4_rows, t5_rows, t6_rows]))

t7_data, t8_data, t9_data = map(lambda t: list(get_data(t[0], t[1])), \
    enumerate([t7_rows, t8_rows, t9_rows]))

t10_data, t11_data, t12_data = map(lambda t: list(get_data(t[0], t[1])), \
    enumerate([t10_rows, t11_rows, t12_rows]))


