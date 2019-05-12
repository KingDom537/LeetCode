# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:47:42 2019

@author: liusi
"""
lens = 1
li = ''
stri = '21'
            # 输出除了最后一位的数
for i in range(len(stri)-1):
    if stri[i] == stri[i+1]:
        lens += 1
    else:
        li += str(lens)+stri[i]
        lens = 1
            #输出最后一位
    if stri[-1] != stri[-2]:
        li += '1'+ stri[-1]
    else:
        i = -1
        lens = 1
        for i in (range(-1,-len(stri)+1,-1)):
            if stri[i] == stri[i-1]:
                lens += 1
            else:
                break
        li += str(lens) + stri[-1]
        stri = li
