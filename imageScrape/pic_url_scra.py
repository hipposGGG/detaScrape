'''
Created on 2020/05/11

@author: Shuhei Takahashi
@note:画像URLスクレイピング編
'''
import requests
import re
import logging
from bs4 import BeautifulSoup


#↓↓↓↓↓サンプル真似たが上手くいかない↓↓↓↓↓
# url = "https://search.nifty.com/imagesearch/search?select=1&q=%s&ss=up"
# keyword = "猫"
# r = requests.get(url%(keyword))
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
logging.basicConfig(filename='D:\eclipse-workspace\python_test\logfile\logger1.log', level=logging.INFO)
r = requests.get("https://www.google.com/search?tbm=isch&q=%E7%8C%AB")
soup = BeautifulSoup(r.text, 'lxml')
imgs = soup.find_all('img', src=re.compile('^https://encrypted-tbn0.gstatic.com/'))
for img in imgs:
    logging.info("画像url:%s", img['src'])
    print(img['src'])

logging.info("★★end★★")