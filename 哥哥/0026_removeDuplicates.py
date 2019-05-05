# -*- coding: utf-8 -*-
"""
时间：2019-04-28
作者：哥哥
题号：0026

题目：
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""

import copy

class Solution(object):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    # 方法1 循环删除数组中多余数字
    def removeDuplicates1(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
    
    # 方法2 循环时跳过重复数字，将不重复的数字按顺序排在数组最前面
    def removeDuplicates2(self, nums):
        # 特殊处理
        if len(nums) == 0:
            return 0
        # 有序数组结尾下标
        index = 0
        # 循环处理
        for i in range(1,len(nums)):
            # 找到一个新的数值
            if nums[index] != nums[i]:
                nums[index+1] = nums[i]
                index += 1
            # 若有序数组的最后一个与整个数组的最后一个相同，则无新数值可添加
            if nums[index] == nums[-1]:
                break
        # index是有序数组下标，下标+1为长度
        return index+1

# 测试用例
printList = [[],[0],[1,1],[0,1],[0,1,2],[0,0,1],[0,1,1],[0,0,0],[0,1,1,2,2,3,3,3],[0,2,4,4,6]]
numList1 = copy.deepcopy(printList)
numList2 = copy.deepcopy(printList)
# 测试结果
slu = Solution()
print('原始数组为',printList)
print('1处理后长度为',list(map(slu.removeDuplicates1, numList1)))
print('1处理后数组为',numList1)
print('2处理后长度为',list(map(slu.removeDuplicates2, numList2)))
print('2处理后数组为',numList2)