'''
@Author: hanchang
@LastModifiedBy: hanchang
'''
import urllib.request
url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
print(response.read())
ur2 = "file:///C:/Users/hconh/Desktop/local.html"
response2 = urllib.request.urlopen(ur2)
print(response2.read())