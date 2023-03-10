from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
import csv
import ssl
import requests
import re
import urllib.request

book = 'gen'
chapter = 1

response = urlopen('https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book=%s&chap=%d'%(book, chapter))
soup = BeautifulSoup(response, 'html.parser')

items = soup.select('div.bible_read')
lis = []
for item in items:
    temp = []
    name = item.select_one('span').text
    # price = item.select_one('div.priceBox > li').text
    # img = item.select_one('a > img')["src"]
    temp.append(name)
    # temp.append(price) 
    # temp.append(img)
    lis.append(temp)

# def saveToFile(filename, shop):    # 저장된 순위를 csv 파일로 저장
with open('bible.csv', 'w', encoding='utf-8-sig',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lis)
f.close

