# -*- coding: utf-8 -*-
"""
时间：2019-04-24
作者：哥哥
题号：0009

题目：
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""

class Solution(object):
    """
    :type x: int
    :rtype: bool
    """

    # 方法1 数字转字符串，反转后判断
    def isPalindrome1(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

    # 方法2 不将数字转为字符串，将数字反向求和后判断是否与原来的相等
    def isPalindrome2(self, x):
        # 若为负数，直接返回False
        if x < 0:
            return False
        # 数字按位拆解
        revX = x
        nums = []
        while revX >= 1:
            bit = revX % 10
            nums.append(bit)
            revX //= 10
        # 反向求和
        for index, value in enumerate(nums):
            revX += value * (10 ** (len(nums) - index - 1))
        # 判断反向后是否相等
        if revX == x:
            return True
        else:
            return False

# 测试用例
nums = [121,-232232,1441,0,37600]
# 测试结果
slu = Solution()
result1 = list(map(slu.isPalindrome1, nums))
result2 = list(map(slu.isPalindrome2, nums))
print('Input List:\n', nums)
print('Output1 List:\n', result1)
print('Output2 List:\n', result2)
