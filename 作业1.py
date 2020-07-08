'''
@Author: 韩畅
@Date: 2020-07-06 20:47:56
@LastEditTime: 2020-07-07 11:23:27
@LastEditors: Please set LastEditors
'''
import urllib.request
url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
print(response.read())
ur2 = "file:///C:/Users/hconh/Desktop/local.html"
response2 = urllib.request.urlopen(ur2)
print(response2.read())