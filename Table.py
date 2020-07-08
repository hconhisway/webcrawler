'''
@Author: 韩畅
@Date: 2020-07-07 11:22:51
@LastEditTime: 2020-07-07 18:31:55
@LastEditors: Please set LastEditors
'''

import pandas as pda
import urllib.request
url = "http://www.maigoo.com/news/463071.html"
response = urllib.request.urlopen(url)
contents = pda.read_html(response)
pda.set_option('display.max_rows',None)#加入这一行设置可以解决行之间出现省略号的问题
x=contents[0]
#print(contents)
contents.append('0')
x = x + '加上的'
x.to_csv('3.csv')
b = '23333'
print(b[0])
print(contents[1])