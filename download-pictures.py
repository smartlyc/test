# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:52:50 2016

@author: SMARTLYC
"""

#import urllib

import urllib2

import requests

from bs4 import BeautifulSoup


#定义函数
#def download（）: （）需考虑是否填参数
def download(url): #必须要注意中英文括号的不同（），(),会提示语法无效
    
    r = requests.get(url)
    
    code = r.status_code
    print code
    if r.status_code !=200:
        
        return
    
    '''url = urllib.quote(url)
    print url
    #url = urllib.unquote(url)
    url = url.replace('%3A',':') '''   
    
       
    filename = url.split('/')[-1].split('.jpg')[0]    
    #filename = url.split('/')[6].split('.jpg')[0]    将6换为-1是考验能力滴
    #print filename    
    #filename = filename.encode('utf-8')
    
    #单独测试时能够解决汉字问题，但是在此项目中无法解决问题
    #filename = urllib.quote(filename) #转换为unicode格式
    #print filename

    #target = './{}.jpg'.format(filename)
    target = './{}.jpg'.format(filename)
    
    #print target
    #target = './hhh111很狠狠.jpg'
    #target = target.decode("utf-8")
    #print target
   
    with open(target,'wb') as fs: #'wb'不可缺少，作用未知
        fs.write(r.content)
        
    return

urls = ['http://news.swjtu.edu.cn/ShowNews-{}-0-1.shtml'.format(number) for number in range(600,800,1)]


for url in urls:

    print url
    
    request =urllib2.Request(url)
    
    response=urllib2.urlopen(request)
    
    soup = BeautifulSoup(response)
        
    pics = soup.select('div > p > img')    #(' p > img')也可以
    
    #pics = soup.select('ul > li > a > img')
    
    for pic in pics:
        src = pic.get('src')
        src = src.replace(' ', '')  ##去除空格
        
        #src = urllib.quote(src)

        http = 'http://'
        if http in src:#:标点符号非常非常容易忘记加，尤其是中间插入if else 语句时！！！
           src = src
        else:          #:标点符号非常非常容易忘记加，尤其是中间插入if else 语句时！！！ 
           src = 'http://news.swjtu.edu.cn'+src

        print src
        
        download(src) #使用函数之前需事先定义函数
        
    
