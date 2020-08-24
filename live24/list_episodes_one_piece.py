from bs4 import BeautifulSoup as bs 
from requests import get


URL = 'https://en.wikipedia.org/wiki/One_Piece_(season_1)#Episode_list'

request = get(URL)

page = bs(request.content, 'lxml')
tables = page.findAll('table', {'class':'wikitable'})

temp_1 = tables


def get_rows(rows):
    return rows.findAll('td')

    
