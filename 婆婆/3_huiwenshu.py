# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:37:47 2019

@author: liusi
"""

#approach 1
def isPalindrome(x):
    x = str(x)
    y = str(x)
    y = y[::-1]
    if x == y:
        return True
    else:
        return False
    
# approach 2
def isPalindrome1(x):
    if x < 0:
        return False
    li = []
    y = x
    while y >= 1:
        a = y % 10
        li.append(a)
        y //= 10
    z = 0
    for index, value in enumerate(li):
        z += value*10**(len(li)-index-1)
    if z == x:
        return True
    else:
        return False
            