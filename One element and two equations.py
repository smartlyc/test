# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 19:38:10 2016

@author: SMARTLYC
"""

#一元二次方程

import random
import math

count =0
while count <5:
    a =random.randint(1,100)
    b =random.randint(1,100)
    c =random.randint(1,100)
    
    #print a+'*X*X+'+b+"X"+c+'=0'
    print a,'*X*X+',b,"X+",c,'=0'
    
    d =b**2-4*a*c
    
    if d<0:
        print '此一元二次方程无解'
    else:
        #x1=(-b+math.sqrt(d))/(2*a)
        #x2=(-b-math.sqrt(d))/(2*a)
        x1=float(-b+math.sqrt(d))/(2*a)
        x2=float(-b-math.sqrt(d))/(2*a)
        print '一元二次方程解为：',x1,'和',x2
    count=count+1
    