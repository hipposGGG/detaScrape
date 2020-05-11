'''
Created on 2020/05/11

@author: Shuhei Takahashi
@note: ページのタイトルをスクレイピング
'''
import requests
from bs4 import BeautifulSoup

# response = requests.get('http://test.neet-ai.com')
response = requests.get('https://www.llsunshine-numazu.jp/')
soup = BeautifulSoup(response.text, 'lxml')
title = soup.title.encoding
print(title)