# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:22:26 2019

@author: liusi
"""

class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] > target:  #target is not biggest
                    return i
            return len(nums)
            
                    
        