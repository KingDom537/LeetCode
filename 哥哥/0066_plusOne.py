# -*- coding: utf-8 -*-
"""
时间：2019-05-05
作者：哥哥
题号：0066

题目：
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""

class Solution(object):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    # 方法1 使用python特性，将list转int，int+1，再将int转list
    def plusOne1(self, digits):
        return list(map(int,str(int(''.join(map(str,digits)))+1)))
    
    # 方法2 直接操作
    def plusOne2(self, digits):
        n = len(digits)
        # 按位加1，若有进位继续加1，若无进位退出循环
        for i in range(n):
            digits[n-i-1] += 1
            if digits[n-i-1] == 10:
                digits[n-i-1] = 0
            else:
                break
        # 若加1后最高为为0，则需要再加一位
        if digits[0] == 0:
            return [1]+digits
        else:
            return digits


        
# 测试用例
testList = [[0],[1],[1,0],[9,9],[1,9,9]]
# 测试结果
slu = Solution()
print(testList,'的运行结果为',list(map(slu.plusOne1,testList)))
print(testList,'的运行结果为',list(map(slu.plusOne2,testList)))
