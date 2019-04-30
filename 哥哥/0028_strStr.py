# -*- coding: utf-8 -*-
"""
时间：2019-04-30
作者：哥哥
题号：0028

题目：
实现strStr()函数
给定一个haystack字符串和一个needle字符串，在haystack字符串中找出needle字符串出现的第一个位置(从0开始)
如果不存在，则返回-1
"""

class Solution(object):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    
    # 方法1 使用python特性
    def strStr1(self, haystack, needle):
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
    
    # 方法2 滑窗判断是否相同
    def strStr2(self, haystack, needle):
        if not needle: return 0
        hLen = len(haystack)
        nLen = len(needle)
        for i in range(hLen - nLen + 1):
            if(haystack[i:i+nLen] == needle):
                return i
        return -1
        

# 测试用例
hStr = 'ajshd 6283nsdfn;laaaasddd'
nStr = 'z'
# 测试结果
slu = Solution()
print(nStr,'在',hStr,'的第',slu.strStr1(hStr, nStr),'位')
print(nStr,'在',hStr,'的第',slu.strStr2(hStr, nStr),'位')
