# -*- coding: utf-8 -*-
"""
时间：2019-04-27
作者：哥哥
题号：0020

题目：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。
3.注意空字符串可被认为是有效字符串。
"""

class Solution(object):
    """
    :type s: str
    :rtype: bool
    """
    
    # 方法1 若是由'()[]{}'构成的有效字符串，必然会有至少1对'()','[]','{}'，
    #       去除成对出现的'()','[]','{}'后的字符串同样必然会有至少1对'()','[]','{}'，
    #       循环这个过程，若最后字符串为空，则为有效字符串
    # 问题  leetcode提交系统判定超时，时间复杂度高
    def isValid1(self, s):
        # 若字符串为奇数个，则必然不是有效字符串
        if len(s)%2 == 1:
            return False
        # 字符串无法删除指定字符，改成list方便操作
        s = list(s)
        # 此次遍历发现了成对出现的'()','[]','{}'
        findFlag = True
        # 直到字符串为空或本次循环没有发现成对出现的'()','[]','{}'，跳出循环
        while (s and findFlag):
            # 遍历一遍字符串
            for i in range(len(s)-1):
                # 去除成对出现的'()','[]','{}'
                if (s[i] == '(' and s[i+1] == ')') or (s[i] == '[' and s[i+1] == ']') or (s[i] == '{' and s[i+1] == '}'):
                    del s[i]
                    del s[i]
                    findFlag = True
                    break
                else:
                    findFlag = False
        return findFlag
    
    # 方法2 原理同方法1一样，使用python特性（借鉴了一下别人的代码~~~）
    # 问题  时间复杂度较高
    def isValid2(self, s):
        if len(s)%2 == 1:
            return False
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}','')
            s = s.replace('()','')
            s = s.replace('[]','')
        return s == ''
    
    # 方法3 使用stack对字符串进行操作，时间复杂度低，
    #      并且可以简单修改后直接对代码进行括号有效性判定
    def isValid3(self, s):
        if len(s)%2 == 1:
            return False
        st = []
        # 循环一遍字符串即可
        for x in s:
            # 若为括号结尾且栈中无元素，则无法匹配此括号结尾，直接判定字符串无效
            if (x == ')' or x == ']' or x == '}') and len(st) == 0:
                return False
            # 若为括号开始，则直接入栈
            if x == '(' or x == '[' or x == '{':
                st.append(x)
            # 若当前元素和栈顶元素可以组成有效括号，则栈顶出栈
            elif (st[-1] == '(' and x == ')') or (st[-1] == '[' and x == ']') or (st[-1] == '{' and x == '}'):
                st.pop()
        # 若栈中无元素，则字符串有效
        return st == []
        

# 测试用例
strList = ['[()]','{[(])}','{[]{()}}[]','','{([]())({([)])}}','{({)','{}][']
# 测试结果
slu = Solution()
print(strList,'-',list(map(slu.isValid1, strList)))
print(strList,'-',list(map(slu.isValid2, strList)))
print(strList,'-',list(map(slu.isValid3, strList)))
