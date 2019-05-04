# -*- coding: utf-8 -*-
"""
时间：2019-05-04
作者：哥哥
题号：0058

题目：
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
"""

class Solution(object):
    """
    :type s: str
    :rtype: int
    """
    
    # 方法1 使用python特性
    def lengthOfLastWord1(self, s):
        s = s.split()
        if not s: return 0
        return len(s[-1])
        
    # 方法2 倒序查找
    def lengthOfLastWord2(self, s):
        head = -1
        tail = -1
        for i in range(len(s)-1,-1,-1):
            if tail == -1 and s[i] != ' ':
                tail = i
            if tail != -1 and s[i] == ' ':
                head = i
                break
        return tail - head

        
# 测试用例
testList = ['',' ','a','asd',' asd','asd ',' asd ','asd asd','asd asd ',' asd asd','  asd  asda']
# 测试结果
slu = Solution()
print(testList,'的运行结果为',list(map(slu.lengthOfLastWord1,testList)))
print(testList,'的运行结果为',list(map(slu.lengthOfLastWord2,testList)))
