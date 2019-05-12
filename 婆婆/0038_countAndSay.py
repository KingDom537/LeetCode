# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:43:41 2019

@author: liusi
"""
def countAndSay(n):
    mark = 2
    if n == 1:
        return '1'
    elif n == 2:
        return '11'
    elif n == 3:
        return '21'
    else:
        mark = 3
        stri = [2,1]
        while mark != n:
            lens = 1
            li = []
            # 输出除了最后一位的数
            for i in range(len(stri)-1):
                if stri[i] == stri[i+1]:
                    lens += 1
                else:
                    li.extend([lens, stri[i]])
                    lens = 1
            #输出最后一位
            if stri[-1] != stri[-2]:
                li.extend([1,stri[-1]])
            else:
                i = -1
                lens = 1
                for i in (range(-1,-len(stri)+1,-1)):
                    if stri[i] == stri[i-1]:
                        lens += 1
                    else:
                        break
                li.extend([lens,stri[-1]])
            stri = li
            mark += 1
        obj = ''
        for x in stri:
            obj += str(x)
        return obj
    

    