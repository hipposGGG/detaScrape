'''
Created on 2020/05/11

@author: Shuhei Takahashi

@note: Pythonでスクレイピングする準備
'''
import requests

# response = requests.get('http://test.neet-ai.com')
response = requests.get('https://www.llsunshine-numazu.jp/')
print(response.text)

# response.encoding = response.apparent_encoding
# print(response.text.encode('utf-8'))
