# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 20:23:00 2016

@author: SMARTLYC
"""

count =0

for i in range(1,10,2):
    count=count+i
print count
print range(10)
print range(5,10)
print range(1,10,2)

# 求变量e

import random
import math
i=random.randint(10,99)
b=1
start=1
i =i+1

#for c in range(1,i)
#c = random.randint(1,i)
for x in range(1,i):
     b=b*x
     start=start+1.0/math.factorial(x)#累乘计算
print 'i=',i,'时，e为：',start

#求 pi

pi=0

for i in range(1,1000005):
    pi=pi+(-1.0)**(i+1)/(2*i-1)
pi=pi*4
print 'pi:',pi