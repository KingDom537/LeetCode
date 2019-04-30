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
    
    # 方法1 利用两层循环进行暴力破解，时间复杂度最大
    def twoSum1(self, nums, target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if((nums[i] + nums[j]) == target):
                    return [i,j]
                
        return []
    
    # 方法2 利用dict()建立哈希查找表，将没有被选中的nums元素加入dic字典中，
    #       后续可直接从dic中查找对应元素，降低循环查找时间，但增加空间复杂度，以空间换时间
    def twoSum2(self, nums, target):
        dic = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in dic:
                return [dic[sub], index]
            dic[value] = index

        return []

# 测试用例
nums = [1,2,3,6,9]
target1 = 5
target2 = 9
# 测试结果
slu = Solution()
result1 = slu.twoSum1(nums, target1)
result2 = slu.twoSum1(nums, target2)
print(result1)
print(result2)
