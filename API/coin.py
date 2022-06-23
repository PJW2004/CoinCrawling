import requests
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/ko/'
html = requests.get(url)
data = BeautifulSoup(html.content, 'html.parser')
coins = ''

ather = []
for x, d in enumerate(data.find('tbody').find_all('tr')):
    
    if x in range(10):
        text_ = d.find(class_='cmc-link')
        coin = text_.find(class_='sc-1eb5slv-0 iworPT').text
        number = text_.find(class_='sc-1teo54s-3 etWhyV').text
        hidden = text_.find(class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text
        coins += f'{number}. {coin}-{hidden}' + '\n'

    else:
        ather.append(d.find(class_='crypto-symbol').text) 

print(coins)
print(f'''그외 : {len(ather)}...
=================================================''')
