# -*- coding: utf-8 -*-
"""
时间：2019-04-26
作者：包包
题号：0001
"""

l = [2,7,11,15,16]
target = 9
lens = len(l)-1

for i in range(0,lens):
    n = 1
    while (i+n) <= lens:
        s = l[i] + l[i+n]
        if s != target:
            n = n+1
            continue
        else:
            print([i,i+n])
            break
            
