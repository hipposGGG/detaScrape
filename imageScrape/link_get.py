'''
Created on 2020/05/11

@author: Shuhei Takahashi
@note: 複数のリンク先をスクレイピング1
'''
import requests
from bs4 import BeautifulSoup

response = requests.get('http://test.neet-ai.com/index2.html')
response = requests.get('https://www.llsunshine-numazu.jp/')
soup = BeautifulSoup(response.text,'lxml')
link = soup.a.get('href')
print(link)