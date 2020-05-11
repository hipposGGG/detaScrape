'''
Created on 2020/05/11

@author: Shuhei Takahashi
@note: twitterのURLを取得
'''
import requests
from bs4 import BeautifulSoup

response = requests.get('http://test.neet-ai.com/index5.html')
soup = BeautifulSoup(response.text,'lxml')
twitter = soup.find('a',id='twitter').get('href')

print(twitter)