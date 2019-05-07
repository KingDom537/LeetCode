# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:13:09 2019

@author: liusi
"""
#approach 1: use python's function directly
class Solution(object):
    def strStr(haystack, needle):
        if needle == "":
            return 0
        else:
            return haystack.find(needle)
#note: str1.find(str2) if false 返回-1; str1.index(str2) if false 返回error
            
#approach2
class Solution1(object):
    def strStr(haystack, needle):
        if needle == "":
            return 0
        else:  #needle首字母是否在haystack中？记录首字母位置
            sign = len(haystack)+1
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    sign = i
                    break
            if sign == len(haystack)+1:
                return -1
            else:
                n = 0
                stop = 0
                while n < len(needle):
                    if needle[:n+1] != haystack[sign:sign+1]:
                        stop =1
                        break
                    if stop == 1:
                        return -1
                    else:
                        n += 1
                if stop == 0:
                    return sign
                        
                    
        