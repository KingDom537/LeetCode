# -*- coding: utf-8 -*-
"""
时间：2019-05-03
作者：哥哥
题号：0053

题目：
给定一个整数数组nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""

class Solution(object):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    # 方法1 3层暴力循环
    def maxSubArray1(self, nums):
        totalSum = nums[0]
        for i in range(1,len(nums)+1):
            for j in range(len(nums)-i+1):
                preSum = sum(nums[j:j+i])
                if preSum > totalSum:
                    totalSum = preSum
        return totalSum
    
    # 方法2 2层暴力循环
    def maxSubArray2(self, nums):
        totalSum = nums[0]
        for i in range(len(nums)):
            preSum = 0
            for j in range(i,len(nums)):
                preSum += nums[j]
                if preSum > totalSum:
                    totalSum = preSum
        return totalSum
    
    # 方法3 动态规划
    def maxSubArray3(self, nums):
        totalSum = nums[0]
        preSum = 0
        for num in nums:
            preSum += num
            if preSum > totalSum:
                totalSum = preSum
            if preSum < 0:
                preSum = 0
        return totalSum

        
# 测试用例
numList = [-3,-1,4,-1,2,1,-5,4]
# 测试结果
slu = Solution()
print(numList,'的连续子数组最大和为',slu.maxSubArray3(numList))
