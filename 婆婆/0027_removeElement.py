# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:29:00 2019

@author: liusi
"""
#LeetCode执行击败了99.78%,比哥哥高0.04% 
class Solution(object):
    def removeElement(nums, val):
        if val not in nums:
            return len(nums)
        else:
            i = 0
            while i < len(nums):
                if nums[i] == val:
                    del nums[i]
                else:
                    i += 1

# approach 2：
    def removeElement2(nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
