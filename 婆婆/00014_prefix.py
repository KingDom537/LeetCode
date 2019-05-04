# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def longestCommonPrefix(strs):   
    #若输入为空
    if not strs: return ""
    #find string with minimum letters
    minstr = min(strs, key = len)
    #用sign1控制大循环
    lens = 0
    sign = 0
    while lens < len(minstr):
        for i in strs:
            if i[:lens+1] != minstr[:lens+1]:
                sign = 1
                break
        if sign == 1:
            break
        else:
            lens += 1
    return minstr[:lens]
            
          
        
    
       
