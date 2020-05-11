'''
Created on 2020/05/11

@author: Shuhei Takahashi

@note: スタンプ設置店舗一覧を CSV ファイルとして出力するのがゴールです。
'''
import re
import requests
import csv
from bs4 import BeautifulSoup

r = requests.get('https://www.llsunshine-numazu.jp/')
html = r.content
soup = BeautifulSoup(html, 'html.parser')
shop_list = soup.find_all('dl', class_=re.compile('^shop_'))

output_list = []
output_list.append(['店名', '情報', 'リンク']) #ヘッダ

for shop in shop_list:
    name = shop.dt.text
    info = shop.dd.text.replace('\n', ' ').replace('\r', ' ')
    link = ''
    if shop.find('a')is not None: # a タグがない場合の対策
        linl = shop.find('a').get('href')
    output_list.append([name, info, link])

with open('shop_list.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f, lineterminator ='\n')
    writer.writerows(output_list)