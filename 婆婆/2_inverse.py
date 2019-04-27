# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:42:07 2019

@author: liusi
"""
# approach 1
a = str(-12340)
new = ''
if a[len(a)-1] == 0:         # new = new[::-1]
    for i in range(len(a)-2, -1, -1):
        new = new + a[i]
else:
    for i in range(len(a)-1, -1, -1):
        new = new + a[i]

if new[-1]=="-":
    new[-1] = ""
    new = -int(new)  # new = "-" + new[:-1]
else:
    new = int(new)
    
if new >= -2**31 and new <= 2**31-1 :
    print(new)
else:
    print(0)

#approach 2
# 对数字从个位开始拆解，再反向求和，最后处理符号和越界
 def reverse(x):
     if x < 0:
         x = -x
         sign = 0
    else:
        sign =1
    #数字拆解
    nums = []
    while x >= 1:
        bit = x % 10
        nums.apend(bit)
        x //= 10
    #反向求和
    for index, value in enumerate(nums):
        x += value*10**(len(nums) - index -1)
    #符号处理
    x = x if sign else -x
    #越界处理
    if x <= 2**31 -1 and x >= -2**31:
        return x
    else:
        return 0
