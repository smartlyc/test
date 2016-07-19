# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:16:58 2016

@author: SMARTLYC
"""

#coding:utf8
import urllib2,urllib
from BeautifulSoup import BeautifulSoup  #导入相应的模块

queryword=raw_input(u"输入查询的字符串:\n".encode('gbk'))
def f(queryword):
    q=lambda x:urllib.quote(x.decode('gbk').encode('utf8')) #lambda 匿名函数
    #encode 编码 / decode 解码  
    
    url="http://www.jiaowu580.com/"
    req=urllib2.Request(url%q(queryword))

    '''req.add_header("User-Agent",r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36")
    req.add_header("X-Requested-With",r'XMLHttpRequest')  '''  
    #req.add_header("User-Agent",r"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36")
    '''req.add_header("X-Requested-With",r'XMLHttpRequest')'''

    res=urllib2.urlopen(req)
    dom=BeautifulSoup(res.read())
    
    table=dom.find("table")
    trs=table.findAll("tr")
    for tr in  trs[2:]:
        print tr.text
f(queryword)