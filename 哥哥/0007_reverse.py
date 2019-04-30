# -*- coding: utf-8 -*-
"""
时间：2019-04-23
作者：哥哥
题号：0007

题目：
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

class Solution(object):
    """
    :type x: int
    :rtype: int
    """

    # 方法1 对数字从个位开始拆解，再反向求和，最后处理符号和越界
    def reverse1(self, x):
        # 符号判别
        if x < 0:
            x = -x
            sign = 0
        else:
            sign = 1
        # 数字按位拆解
        nums = []
        while x >= 1:
            bit = x % 10
            nums.append(bit)
            x //= 10
        # 反向求和
        for index, value in enumerate(nums):
            x += value * (10 ** (len(nums) - index - 1))
        # 符号处理
        x = x if sign else -x
        # 数字越界处理
        if x <= 2 ** 31 - 1 and x >= -(2 ** 31):
            return x
        else:
            return 0

    # 方法2 利用Python特性，将数字转成字符，反转后，处理符号和越界，再转回数字
    def reverse2(self, x):
        # 转字符
        x = str(x)
        # 反转
        x = x[::-1]
        # 符号处理
        if x[-1] == '-':
            x = '-' + x[:-1]
        # 转数字
        x = int(x)
        # 数字越界处理
        if x <= 2 ** 31 - 1 and x >= -(2 ** 31):
            return x
        else:
            return 0

# 测试用例
nums = [12,20,3123,-6,0,-137600]
# 测试结果
slu = Solution()
result1 = list(map(slu.reverse1, nums))
result2 = list(map(slu.reverse2, nums))
print('Input list:\n',nums)
print('Output1 list:\n',result1)
print('Output2 list:\n',result2)

