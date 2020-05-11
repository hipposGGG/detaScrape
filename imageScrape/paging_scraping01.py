'''
Created on 2020/05/11

@author: Shuhei Takahashi
@note: https://news.nifty.com/で検索
'''
import requests

for page in range(1,11):
    r = requests.get("https://news.nifty.com/technology/" + str(page))
    r.encoding = r.apparent_encoding
    print(r.text)