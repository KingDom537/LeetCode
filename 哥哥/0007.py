# -*- coding: utf-8 -*-
"""
时间：2019-04-23
作者：哥哥
题号：0007

题目：
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

class Solution(object):
    """
    :type x: int
    :rtype: int
    """
    def reverse1(self, x):
        if x < 0:
            x = -x
            sign = 0
        else:
            sign = 1

        nums = []
        while x >= 1:
            bit = x % 10
            nums.append(bit)
            x //= 10

        result = 0
        for index, value in enumerate(nums):
            result += value * (10 ** (len(nums) - index - 1))
        result = result if sign else -result

        if result <= 2 ** 31 - 1 and result >= -(2 ** 31):
            return result
        else:
            return 0

    def reverse2(self, x):
        x = str(x)
        x = x[::-1]
        if x[-1] == '-':
            x = '-' + x[:-1]
        x = int(x)
        if x <= 2 ** 31 - 1 and x >= -(2 ** 31):
            return x
        else:
            return 0


nums = [12,20,3123,-6,0,-137600]
slu = Solution()
result = list(map(slu.reverse2, nums))
print('Input list:\n',nums)
print('Output list:\n',result)
