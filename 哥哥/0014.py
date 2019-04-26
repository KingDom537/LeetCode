# -*- coding: utf-8 -*-
"""
时间：2019-04-26
作者：哥哥
题号：0014

题目：
编写一个函数来查找字符串数组中的最长公共前缀，如果不存在公共前缀，
返回空字符串 ""，所有输入只包含小写字母 a-z 。
"""

class Solution(object):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    # 方法1 选出最短的字符串，从头扫描到尾
    def longestCommonPrefix1(self, strs):
        # 输入为空时特殊处理
        if not strs: return ""
        # 寻找最短字符串
        minStr = min(strs, key = len)
        # 公共长度
        matchLen = 0
        matchStop = 0
        # 遍历每个字符位
        while matchLen < len(minStr):
            # 遍历每个字符串
            for s in strs:
                if s[:matchLen+1] != minStr[:matchLen+1]:
                    matchStop = 1
                    break
            if matchStop == 1:
                break
            else:
                matchLen += 1
        return minStr[:matchLen]
    
    # 方法2 min和max分别返回字符串按字典排序后的最小字符和最大字符
    #      例如：ab,abc,ba,c之中，min = ab, max = c
    #      min和max代表字符串数组差距最大的字符串，其公共字符串为字符串数组的公共字符串
    def longestCommonPrefix2(self, strs):
        if not strs: return ""
        smin = min(strs)
        smax = max(strs)
        for index, value in enumerate(smin):
            if value != smax[index]:
                return smin[:index]
        return smin


# 测试用例
strList1 = ["list","listtong",'lisa']
strList2 = ["liusi","","liusy"]
strList3 = ["asd","qwe","asf"]
strList4 = []
# 测试结果
slu = Solution()
print(strList1,'的公共前缀为',slu.longestCommonPrefix1(strList1))
print(strList2,'的公共前缀为',slu.longestCommonPrefix1(strList2))
print(strList3,'的公共前缀为',slu.longestCommonPrefix1(strList3))
print(strList4,'的公共前缀为',slu.longestCommonPrefix1(strList4))

