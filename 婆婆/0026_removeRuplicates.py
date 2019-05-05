# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:23:02 2019

@author: liusi
"""

def removeDuplicates(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i+1]
        else:
            i += 1
    return len(nums)