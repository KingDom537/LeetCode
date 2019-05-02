# -*- coding: utf-8 -*-
"""
时间：2019-05-02
作者：哥哥
题号：0038

题目：
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
6.     312211
7.     13112221
8.     1113213211
9.     31131211131221

1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
"""

class Solution(object):
    
    # 解析字符串
    def str2ListInGroup(self, strIn):
        # 将字符串按数字分组
        result = []
        group = [strIn[0]]
        for i in range(1,len(strIn)):
            if strIn[i] == strIn[i-1]:
                group.append(strIn[i])
            else:
                result.append(group)
                group=[strIn[i]]
        result.append(group)
        # 生成新的字符串
        strOut = ''
        for l in result:
            strOut += str(len(l)) + str(l[0])
        return strOut
    
    """
    :type n: int
    :rtype: str
    """
    
    # 要求n对应的字符串，先求n-1对应的字符串，
    # 要求n-1对应的字符串，先求n-2对应的字符串，
    # ......
    # 要求2对应的字符串，先求1对应的字符串
    # 1对应的字符串为'1'
    def countAndSay(self, n):
        if n == 1:
            return '1'
        return self.str2ListInGroup(self.countAndSay(n-1))


# 测试用例
num = 6
# 测试结果
slu = Solution()
print(num,':',slu.countAndSay(num))
