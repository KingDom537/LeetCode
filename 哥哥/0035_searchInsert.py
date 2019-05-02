# -*- coding: utf-8 -*-
"""
时间：2019-05-02
作者：哥哥
题号：0035

题目：
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
"""

class Solution(object):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    # 暴力求解
    def searchInsert1(self, nums, target):
        if target in nums:
            return nums.index(target)
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)
    
    # 二分法求解
    def searchInsert2(self, nums, target):
        s = 0
        e = len(nums)-1
        while s <= e:
            mid = (e+s)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return s
        
        

# 测试用例
numList = [1,3,5,6,8]
num = 9
# 测试结果
slu = Solution()
print('应该把',num,'放在',numList,'的第',slu.searchInsert2(numList, num),'位')
