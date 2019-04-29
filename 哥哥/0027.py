# -*- coding: utf-8 -*-
"""
时间：2019-04-29
作者：哥哥
题号：0027

题目：
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变,你不需要考虑数组中超出新长度后面的元素。
"""

class Solution(object):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    # 方法1 使用python特性
    def removeElement1(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)

    # 方法2 从头找等于val的位子，再从尾找不为val的数，将尾的数赋到头的位子里，
    #       循环到头尾下标相同(LeetCode执行用时击败99.74%)
    def removeElement2(self, nums, val):
        headIndex = 0
        tailIndex = len(nums)-1
        # 头下标循环
        while headIndex <= tailIndex:
            if(nums[headIndex] != val):
                headIndex += 1
            else:
                # 尾下标循环
                while tailIndex >= headIndex:
                    if(nums[tailIndex] == val):
                        tailIndex -= 1
                    else:
                        nums[headIndex] = nums[tailIndex]
                        headIndex += 1
                        tailIndex -= 1
                        break
        return headIndex

# 测试用例
numList = [0,3,1,2,6,0,7,9,0,0,0,8,0,0,5,4]
val = 0
# 测试结果
slu = Solution()
print('原始数组为',numList)
print('处理后长度为',slu.removeElement2(numList, val))
print('处理后数组为',numList)
