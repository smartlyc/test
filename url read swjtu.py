# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:52:50 2016

@author: SMARTLYC
"""

import urllib2
from bs4 import BeautifulSoup

#request =urllib2.request("http://www.swjtu.edu.cn/")#Request 首字母大写
request =urllib2.Request("http://www.jiaowu580.com/")
#request =urllib2.Request("https://www .zhihu.com/")

response=urllib2.urlopen(request)

#response = urllib2.urlopen("http://www.swjtu.edu.cn")---
#www.swjtu.edu.cn 无法打开，原因不详，后先尝试打开百度首页成功，再尝试交大首页，竟然成功了

soup = BeautifulSoup(response)

#print (soup.prettify())

print 'soup.title =',soup.title

print 'soup.title.name =',soup.title.name

print 'soup.title.string =',soup.title.string

print 'soup.title.parent.name = ',soup.title.parent.name

print 'soup.p =',soup.p

print 'soup.a =',soup.a

print 'soup.find_all(\'a\') =',soup.find_all('a')

print 'soup.find(id = \"link1\") =',soup.find(id="link1")  #存在问题，未解决

count=1
print 'soup.find_all(\'a\') :'  #转义字符的使用
for link in soup.find_all('a'):
    print count,(link.get('href'))
    count=count+1

print 'soup.find_all(\'b\') =',soup.find_all('b') 

print 'soup.find(\".jpg\") =',soup.find(".jpg")  #存在问题，未解决

   
#print (soup.get_text())  #输出内容占用篇幅很狠狠大，建议不与其他内容同时输出




# print 'soup.p [‘class’] =',soup.p[‘class’]  出现问题调试不通




#print response.read()
