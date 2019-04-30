# -*- coding: utf-8 -*-
"""
时间：2019-04-25
作者：哥哥
题号：0013

题目：
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
"""

class Solution(object):
    """
    :type s: str
    :rtype: int
    """
    
    # 罗马数字转数值
    def romanToInt(self, s):
        # 查找表
        table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)):
            # 不为最后一个字母，且比下一个字母小
            if i < len(s)-1 and table[s[i]] < table[s[i+1]]:
                result -= table[s[i]]
            # 正常情况
            else:
                result += table[s[i]]
        # 返回结果
        return result

    # 数值转罗马数字
    def intToRoman(self, num):
        # 查找表
        table = {0:("","I","II","III","IV","V","VI","VII","VIII","IX"),
                 1:("","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"),
                 2:("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"),
                 3:("","M","MM","MMM")}
        # i代表位数，也即查找表的index值
        i = 0
        strList = []
        # 循环条件为找到num的所有位
        while num >= 1:
            # bit为当前位上的值
            bit = num % 10
            # 根据当前位和当前值对应查找表，加到list尾
            strList.append(table[i][bit])
            # 去掉num的最低位，位数+1
            num //= 10
            i += 1
        # join将list拼接，此处反向拼接
        return "".join(strList[::-1])
            
            

# 测试用例
romanNum = 'MCMXCIV'
intNum = 1994
# 测试结果
slu = Solution()
print(romanNum,'对应数值为',slu.romanToInt(romanNum))
print(intNum,'对应罗马数字为',slu.intToRoman(intNum))



