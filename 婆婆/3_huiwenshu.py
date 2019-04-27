# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:37:47 2019

@author: liusi
"""
import copy

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
    elif x == 0:
        return True
    else:
        if x % 10 == 0:
            return False
        else:
            li = []
            y = copy.copy(x)
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
            