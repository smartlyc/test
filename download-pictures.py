# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:52:50 2016

@author: SMARTLYC
"""

#import urllib

import chardet

import urllib2

import requests

from bs4 import BeautifulSoup

#方法1.设置运行时的默认编码,可以解决图片.jpg，UnicodeEncodeError: 'ascii' codec can't encode characters in position 35-36: ordinal not in range(128)
#存在不足，部分网页图片存取依旧报错
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

# 定义函数
# 将所以 print 内容保存到 debug_log.txt
def debug_log(info):
    
    path = './debug_log.txt'
    
    print type(info).__name__
    
    # 判断编码类型是否为 unicode ,包含中文需要将unicode 转换为 GB2312格式
    if type(info).__name__=="unicode" :  # and or 须分清
       info = info.encode("utf8")
    
    # int dict 转 str  
    if type(info).__name__ == "int" or type(info).__name__ =='dict': # == 符号切记不可以使用 =
       info = str(info)  # int 转 str
    
    #info = info.decode('utf8')
       
    with open(path,'a+') as f:  # 'w' 仅仅只会保存1129这一条网址，其他的都被覆盖掉了，'a+' 追加模式
        f.write(info)
        f.write('\n')
    return


#定义函数
#def download（）:
def download(url): #必须要注意中英文括号的不同（），(),会提示语法无效
    
    r = requests.get(url)
    
    code = r.status_code
    #code = str(code) # 传入debug_log()的参数必须为字符串
    print code
    debug_log(code)    
    
    if r.status_code !=200:
        
        return
    
    
    filename = url.split('/')[-1].split('.jpg')[0]    
    #filename = url.split('/')[6].split('.jpg')[0]    将6换为-1是考验能力滴
    print 'filename ='+filename,'type(filename).__name__='+type(filename).__name__   
    # filename 中包含中文时编码格式为 utf-8
    filename = filename.encode("utf-8")    
    print 'filename ='+filename,'type(filename).__name__='+type(filename).__name__   

    
    #单独测试时能够解决汉字问题，但是在此项目中无法解决问题
    #filename = urllib.quote(filename) #转换为unicode格式

    target = '../pic/{}.jpg'.format(filename)
    print 'target=',target
    #target = './{}.jpg'.format(filename)    图片存储路径设置
    chardet_target = chardet.detect(target)
    #chardet_target = str(chardet_target)  # 传入debug_log()的参数必须为字符串
    print chardet_target
    debug_log(chardet_target)    
    
    # print chardet.detect(target) 为 {'confidence': 0.7525, 'encoding': 'utf-8'}  需要转换为unicode编码  使用decode()
    #target = target.decode("utf-8")   #方法2.也可以可以解决图片.jpg，UnicodeEncodeError: 'ascii' codec can't encode characters in position 35-36: ordinal not in range(128)
   
    if type(target).__name__!="unicode":
      target = unicode(target,'utf8')  #路径中包含中文时的 处理方法，与 target = target.decode("utf-8") 作用相同
   
    with open(target,'wb') as fs: #'wb'不可缺少，作用未知,'r' 'w' 两种模式，read 和 write
        fs.write(r.content)
     
    return


# 主函数
#  u'' 字符串在内存中编码格式为unicode  ,此处是否加 u 都可以
urls = [u'http://news.swjtu.edu.cn/ShowNews-{}-0-1.shtml'.format(number) for number in range(840,12000)]


for url in urls:

    print url
    debug_log(url)            
    
    request =urllib2.Request(url)
    
    response =urllib2.urlopen(request)
    
    soup = BeautifulSoup(response)
        
    pics = soup.select('div > p > img')    #(' p > img')也可以
    
    #pics = soup.select('ul > li > a > img')
    
    for pic in pics:
        src = pic.get('src')
        src = src.replace(' ', '')  ##去除空格
        
        http = 'http://'
        if http in src:#:标点符号非常非常容易忘记加，尤其是中间插入if else 语句时！！！
           src = src
        else:          #:标点符号非常非常容易忘记加，尤其是中间插入if else 语句时！！！ 
           src = 'http://news.swjtu.edu.cn'+src

        print src
        debug_log(src)        
        
        download(src) #使用函数之前需事先定义函数
        
    
