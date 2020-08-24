from calendar import monthrange
from requests import get
from bs4 import BeautifulSoup as bs

base_url = 'https://www.calendarr.com/brasil/calendario-janeiro-2020/'

page = bs(get(base_url).text, 'lxml')

table = page.find('ul', {'class':'list-holidays'})
days = page.find_all('li', {'class':'list-holiday-box'})

def is_off(bs_day):
    if bs_day.find('div', {'class':'list-holiday-dayweek holyday'}):
        return True
    return bs_day.text.split()[1] in ['sab', 'dom']

def get_day(bs_day):
    """Get number of the day."""
    return bs_day.text.split()[0]

offdays = set(map(int, map(get_day, filter(is_off, days))))
days = set(range(1, monthrange(2020, 1)[1])) - offdays