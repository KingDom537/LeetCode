# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:13:09 2019

@author: liusi
"""
#approach 1: use python's function directly
class Solution(object):
    def strStr(haystack, needle):
        if needle == "":   # if not needle
            return 0
        else:
            return haystack.find(needle)
#note: str1.find(str2) if false 返回-1; str1.index(str2) if false 返回error
            
#approach2
class Solution1(object):
    def strStr(haystack, needle):
        if not needle:
            return 0
        else:
            hlen = len(haystack)
            nlen = len(needle)
            sign = 0
            # 将needle视为一个整体，在haystack上滑动比对
            for i in range(hlen-nlen+1):
                if haystack[i:i+nlen] == needle:
                    sign  = 1  # retrun i
                    break
            if sign == 1:  # return -1
                return i
            else: 
                return -1
                
                        
                    
        