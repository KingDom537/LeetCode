# -*- coding: utf-8 -*-
"""
时间：2019-05-07
作者：哥哥
题号：0069

题目：
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

牛顿迭代法
f(x)=x^2-t
当f(x)=0时，x就为t的平方根
取(t,f(t))作为切点，取切线，切线与x轴相交点为x0
切线方程：y1 - f(x0) = f(x0)'(x1 - x0); 令y1=0
得：x1 = x0 / 2 + t / (2*x0);
取(x0,f(x0))作为切点，取切线，切线与x轴相交点为x1
重复上述操作
最后切点为(xn,f(xn))，此时f(xn)近似于0，xn为平方根
"""

import math

class Solution(object):
    """
    :type x: int
    :rtype: int
    """
    
    # 方法1 使用math函数
    def mySqrt1(self, x):
        return int(math.sqrt(x))
    
    # 方法2 穷举
    def mySqrt2(self, x):
        for i in range(x+1):
            if i**2<=x and (i+1)**2>x:
                return i

    # 方法3 牛顿迭代法
    def mySqrt3(self, x):
        if x <= 1: return x
        r = x
        while r > x/r:
            r = (r + x/r) // 2
        return int(r)


# 测试用例
testList = [0,1,2,3,4,9,100,101,2147395599]
# 测试结果
slu = Solution()
print(testList,'的运行结果为',list(map(slu.mySqrt1,testList)))
print(testList,'的运行结果为',list(map(slu.mySqrt2,testList)))
print(testList,'的运行结果为',list(map(slu.mySqrt3,testList)))
