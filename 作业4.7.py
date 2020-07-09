'''
@Author: hanchang
@LastModifiedBy: hanchang
'''
import urllib.request
from bs4 import BeautifulSoup
import codecs
import re

import urllib.request
from bs4 import BeautifulSoup

url = "http://www.xiexingcun.com/ertong/index57.htm"
response = urllib.request.urlopen(url)

soup=BeautifulSoup(response,'html.parser')

x=soup.find(style="border-style: none; border-width: medium; ")
for link in soup.find_all('a'):
    x=link.get('href')
    r2=re.compile('wangerde',re.I)

    if r2.search(x):
        lianJie = link.get('href')
        mingCheng = link.text

        resp = urllib.request.urlopen('http://www.xiexingcun.com/ertong/'+str(lianJie))
        soup2=BeautifulSoup(resp,'html.parser')
        x2=soup2.find(style="border-style: none; border-width: medium; ")
        y2 = x2.get_text()
        f = codecs.open("王尔德童话.txt","a","utf-8-sig")
        f.write(str(mingCheng))
        f.write(y2)
        f.close()




