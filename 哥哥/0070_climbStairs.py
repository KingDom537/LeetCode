# -*- coding: utf-8 -*-
"""
时间：2019-05-08
作者：哥哥
题号：0070

题目：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
"""

class Solution(object):
    """
    :type n: int
    :rtype: int
    """
    
    # 递归
    def climbStairs1(self, n):
        # 0层台阶有0种爬法
        # 1层台阶只有1种爬法
        # 2层台阶有2种爬法
        if n < 3: return n
        # 3层台阶时，若只考虑第一下，有两种爬法，爬1层或爬2层，剩下2层台阶或1层台阶
        # 4层台阶时，若只考虑第一下，有两种爬法，爬1层或爬2层，剩下3层台阶或2层台阶
        # ...
        # n-1层台阶时，若只考虑第一下，有两种爬法，爬1层或爬2层，剩下n-2层台阶或n-3层台阶
        # n层台阶时，若只考虑第一下，有两种爬法，爬1层或爬2层，剩下n-1层台阶或n-2层台阶
        return self.climbStairs1(n-1)+self.climbStairs1(n-2)
        
    # 循环，计算斐波那契数列
    def climbStairs2(self, n):
        if n < 3: return n
        back2,back1 = 1,2
        for i in range(n-2):
            back2,back1 = back1, back2+back1
        return back1


# 测试用例
testList = [0,1,2,3,4,5,6,7,8,9,10]
# 测试结果
slu = Solution()
print(testList,'的运行结果为',list(map(slu.climbStairs1,testList)))
print(testList,'的运行结果为',list(map(slu.climbStairs2,testList)))
