'''
Created on 2020/05/11

@author: Shuhei Takahashi
@note: リンク先をスクレイピング
'''
import requests
from bs4 import BeautifulSoup

# response = requests.get('http://test.neet-ai.com')
response = requests.get('https://www.llsunshine-numazu.jp/')
soup = BeautifulSoup(response.text, 'lxml')
link = soup.a.get('href')
print(link)
