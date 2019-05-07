# -*- coding: utf-8 -*-
"""
时间：2019-05-06
作者：哥哥
题号：0067

题目：
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。
"""

class Solution(object):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    
    # 方法1 使用python特性
    def addBinary1(self, a, b):
        return bin(int(a,2)+int(b,2))[2:]
    
    def addBinary2(self, a, b):
        # 结果字符串
        result = ''
        # 进位
        cin = 0
        # 分别从a和b的尾开始循环
        indexA = len(a)-1
        indexB = len(b)-1
        # 循环到a和b都结束才退出循环
        while indexA>=0 or indexB>=0:
            # 当前位a的值，若a已经结束b未结束，补0
            if indexA >= 0:
                bitA = int(a[indexA])
            else:
                bitA = 0
            # 当前位b的值，若b已经结束a未结束，补0
            if indexB >= 0:
                bitB = int(b[indexB])
            else:
                bitB = 0
            # 当前位相加和
            s = bitA + bitB + cin
            # 进位
            cin = s // 2
            # 当前为结果值
            s %= 2
            # 当前位结果值存入
            result = str(s) + result
            # 循环递减
            indexA -= 1
            indexB -= 1
        # 若仍有进位，再补一个1
        if cin:
            result = '1' + result
        # 返回结果
        return result


# 测试用例
testA = '11'
testB = '11'
# 测试结果
slu = Solution()
print(testA,'+',testB,'的运行结果为',slu.addBinary1(testA, testB))
print(testA,'+',testB,'的运行结果为',slu.addBinary2(testA, testB))
