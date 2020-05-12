'''
Created on 2020/05/11

@author: Shuhei Takahashi
@note:画像URLスクレイピング編～google.ver～
'''
import requests
import re
import uuid
import logging
import urllib
from bs4 import BeautifulSoup

logging.basicConfig(filename='D:\eclipse-workspace\python_test\logfile\logger1.log', level=logging.INFO)
query = 'リナリー'
url = "https://www.google.co.jp/search?q="+urllib.parse.quote(query)+"&source=lnms&tbm=isch"
# r = requests.get("https://www.google.com/search?tbm=isch&q=%E7%8C%AB")
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
print(soup)
imgs = soup.find_all('img', src=re.compile('^https://encrypted-tbn0.gstatic.com/'))
for img in imgs:
    logging.info("画像url:%s", img['src'])
    print(img['src'])
    r = requests.get(img['src'])
    with open(str('./picture/')+ str(uuid.uuid4())+ str('.jpeg'), 'wb') as file:
        file.write(r.content)

logging.info("★★end2★★")