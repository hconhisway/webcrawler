'''
@Author: 韩畅
@Date: 2020-07-06 20:47:56
@LastEditTime: 2020-07-06 20:49:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \webcrawler-1\作业1.py
'''
import urllib.request
url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
print(response.read())
ur2 = "http://google.com"
response2 = urllib.request.urlopen(ur2)
print(response2.read())
