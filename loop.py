# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 19:07:15 2016

@author: SMARTLYC
"""

count=0
import random   #声明调用random函数

while count <5:
    print count+1
    print random.randint(100,999)
    print 'hello world'
    print random.randint(100,999),'hello world'
    count =count+1
    