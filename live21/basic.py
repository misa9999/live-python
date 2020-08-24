from selenium import webdriver
from bs4 import BeautifulSoup as bs

class Page:
    def __init__(self, driver):
        self.driver = driver

    
go = webdriver.Chrome()
go.get('http://google.com')
html = go.page_source