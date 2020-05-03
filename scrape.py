'''
Created on 2020/04/29

@author: USER
'''
import bs4
import requests
import re
import urllib.request, urllib.error
import os
import argparse
import sys
import json
import codecs
import logging


# How To
# (1) ソースコードを保存して命名する (e.g. scrape.py)
# (2) プログラムを起動する python scrape.py
# (3) オプション
# -s: Google Imagesにかける検索キーワード、複数可 (デフォルト "banana")
# -n: ダウンロードする画像の数量 (デフォルト 10枚)
# -o: 画像の保存先 (デフォルト　<DEFAULT_SAVE_DIRECTORY>で指定する)
logging.basicConfig(filename='D:\eclipse-workspace\python_test\logfile\logger.log', level=logging.INFO)

def get_soup(url,header):
    return bs4.BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

def main(args):
    DEFAULT_SAVE_DIRECTORY = 'D:\eclipse-workspace\python_test\scrape'
    parser = argparse.ArgumentParser(description='Options for scraping Google images')
    parser.add_argument('-s', '--search', default='banana', type=str, help='search term')
    parser.add_argument('-n', '--num_images', default=10, type=int, help='num of images to scrape')
    parser.add_argument('-o', '--directory', default=DEFAULT_SAVE_DIRECTORY, type=str, help='output directory')
    args = parser.parse_args()

    # 複数のキーワードを"+"で繋げる
    query = args.search.split()
    logging.info("1回目： %s",query)
    query = '+'.join(query)
    logging.info("2回目： %s",query)
    max_images = args.num_images
    logging.info("max_images： %s",max_images)

    # 画像をフォルダーでグループする
    save_directory = args.directory + '\\' + query
    logging.info("save_directory： %s",save_directory)
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
#     save_directory = "D:\eclipse-workspace\python_test\scrape\cat"
#     if not os.path.exists(save_directory):
#         os.makedirs(save_directory)

    # スクレーピング Chrome/43.0.2357.134
    url="https://www.google.co.jp/search?q="+urllib.parse.quote(query)+"&source=lnms&tbm=isch"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}
    logging.info("url： %s",url)
    logging.info("header： %s",header)
    soup = get_soup(url,header)
    ActualImages=[]
#     logging.info("souptmp： %s",souptmp)
#     print("★soup:",soup)
#     soup = souptmp.decode('utf-8')
#     logging.info("soup： %s",soup)
    print("★soup★",soup)

#     for a in (soup.decode('utf-8')).find_all("div",{"class":"rg_meta"}):
    #ここから処理詳細追えていない
    #↓↓↓↓↓↓↓↓↓↓↓↓↓
    # 要素名が div でclass_またはrg_metaを含む要素を抽出
    for a in soup.find_all("div",{"class_":"rg_meta"}):
        logging.info("a： %s",a)
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))
    for i , (img , Type) in enumerate( ActualImages[0:max_images]):
        try:
            Type = Type if len(Type) > 0 else 'jpg'
            print("Downloading image {} ({}), type is {}".format(i, img, Type))
            raw_img = urllib.request.urlopen(img).read()
            f = open(os.path.join(save_directory , "img_"+str(i)+"."+Type), 'wb')
            f.write(raw_img)
            f.close()
        except Exception as e:
            print ("could not load : "+img)
            print (e)

if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()