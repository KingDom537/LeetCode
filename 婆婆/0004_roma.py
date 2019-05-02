# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:43:22 2019

@author: liusi
"""
# approach 1
class Solution(object):
    def romanToInt(self, li):
        dict1 = {'I' : 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
         'IV':4,'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        num = []

        while len(li) > 1:
            if dict1.get(li[0]) >= dict1.get(li[1]):
               num.append(li[0])
               li = li[1:]
            else:
                a = li[0]+li[1]
                num.append(a)
                li = li[2:]

        if len(li) == 1:
            num.append(li)

        summ = 0
        for i in num:
            summ += dict1.get(i)
        return summ
    
#approach 2
        
class Solution(object):
    def romanToInt(self, li):
        dict1 = {'I' : 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        summ = 0
        for i in range(0,len(li)):
            if i < (len(li)-1) and dict1[li[i]] < dict1[li[i+1]]:
                summ -= dict1[li[i]]
            else:
                summ += dict1[li[i]]
        return summ
    

        
        