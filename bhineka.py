from requests import get
from bs4 import BeautifulSoup

url= 'https://shopee.co.id/search'
param = {'keyword':'xiaomi'}
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

html_text = get(url,params=param,headers=header)
soup = BeautifulSoup(html_text.text, 'html.parser')
cari = soup.find(attrs={'class':'row shopee-search-item-result__items'})

print(cari)