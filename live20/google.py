"""Exemplo de PO no google.com"""
from selenium import webdriver


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com'
        self.search_bar = 'q' # name
        self.btn_search = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]' # xpath
        self.img_search = '//*[@id="hdtb-msb-vis"]/div[2]/a' # xpath
        self.btn_lucky = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[2]' # xpath

        # self.url = 'http://youtube.com'
        # self.search_bar = 'search' # name
        # self.btn_search = 'search-icon-legacy' # name

    
    def navigate(self):
        self.driver.get(self.url)


    def search(self, word='None'):
        self.driver.find_element_by_name(self.search_bar).send_keys(word)
        self.driver.find_element_by_xpath(self.btn_search).click()
        # self.driver.find_element_by_xpath(self.img_search).click()

    def lucky(self, word='None'):
        self.driver.find_element_by_xpath(self.search_bar).send_keys(word)
        self.driver.find_element_by_xpath(self.btn_lucky).click()


    # def lucky(self, word='None'):
    #     self.driver.find_element_by_name(
    #         self.search_bar).send_keys(word)
    #     self.driver.find_element_by_name(
    #         self.btn_lucky).click()



ff = webdriver.Chrome()
g = Google(ff)
g.navigate()
g.search('Live de python')