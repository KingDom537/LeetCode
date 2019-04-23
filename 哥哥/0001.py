# -*- coding: utf-8 -*-
"""
时间：2019-04-23
作者：哥哥
题号：0001

题目：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

class Solution(object):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    def twoSum1(self, nums, target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if((nums[i] + nums[j]) == target):
                    return [i,j]
                
        return []
    
    def twoSum2(self, nums, target):
        dic = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in dic:
                return [dic[sub], index]
            dic[value] = index

        return []

nums = [1,2,3,6,9]
target = 5
slu = Solution()
result = slu.twoSum2(nums, target)
print(result)


