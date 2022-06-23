import requests
from bs4 import BeautifulSoup

class look:

    def __init__(self, coinname=None):
        if ' ' in coinname:
            coinname = coinname.replace(' ', '-')
        self.url = f'https://coinmarketcap.com/ko/currencies/{coinname}/'
        html = requests.get(self.url)
        self.data = BeautifulSoup(html.content, 'html.parser')

    def real_time(self):
        try:
            market_conditions = self.data.find(class_='priceValue smallerPrice').text
        except AttributeError:
            market_conditions = self.data.find(class_='priceValue').text
            
        try:
            percent = self.data.find(class_='sc-15yy2pl-0 gEePkg').text
        except AttributeError:
            percent = self.data.find(class_='sc-15yy2pl-0 feeyND').text
        
        return market_conditions, percent, self.url

