'''
Created on 2020/05/11

@author: Shuhei Takahashi
@note:画像URLスクレイピング編～google.ver～
'''
import requests
import re
import uuid
import os
import logging
import urllib
import sys
import argparse
from bs4 import BeautifulSoup

#デフォルトの保存格納先
DEFAULT_SAVE_DIRECTORY = 'D:\eclipse-workspace\python_test\imageScrape\img'

def main(args):
    #ログの出力先指定
    logging.basicConfig(filename='D:\eclipse-workspace\python_test\logfile\logger1.log', level=logging.INFO)

    parser = argparse.ArgumentParser(description='Options for scraping Google images')
    #検索キーワードの入力値。デフォルトで「バナナ」
    parser.add_argument('-s', '--search', default='banana', type=str, help='search term')
    parser.add_argument('-o', '--directory', default=DEFAULT_SAVE_DIRECTORY, type=str, help='output directory')
    args = parser.parse_args()

    #入力した検索キーワード
    query = args.search.split()
    #入力した検索キーワードで別個ファイルを作成
    save_directory = args.directory + '\\' + query[0]
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    url = "https://www.google.co.jp/search?q="+urllib.parse.quote(query[0])+"&source=lnms&tbm=isch"
    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml')
    #'img'をキーとし引数２で画像URLを取得
    imgs = soup.find_all('img', src=re.compile('^https://encrypted-tbn0.gstatic.com/'))

    for img in imgs:
        logging.info("画像url:%s", img['src'])
        print(img['src'])
        r = requests.get(img['src'])
#         with open(str('./img/')+ str(uuid.uuid4())+ str('.jpeg'), 'wb') as file:
        with open(save_directory +'/'+ str(uuid.uuid4())+ str('.jpeg'), 'wb') as file:
            file.write(r.content)

    logging.info("★★end2★★")


if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()