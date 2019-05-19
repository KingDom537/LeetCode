# -*- coding: utf-8 -*-
"""
时间：2019-05-19
作者：哥哥
题号：0086

题目：
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
"""

class Solution(object):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    
    # 方法1 循环+移位
    def merge1(self, nums1, m, nums2, n):
        index1 = 0
        index2 = 0
        # nums2中若有需要插空放进nums1中的，循环遍历处理
        while index1 < m and index2 < n:
            if nums1[index1] > nums2[index2]:
                nums1[index1+1:m+1] = nums1[index1:m]
                nums1[index1] = nums2[index2]
                index2 += 1
                m += 1
            index1 += 1
        # 若nums2中仍有剩余数字，直接赋值
        if index2 != n:
            nums1[m:m+n-index2] = nums2[index2:n]
    
    # 方法2 倒序处理
    def merge2(self, nums1, m, nums2, n):
        while n > 0:
            # nums2中的值大于nums1中的值，或nums1循环到头
            if nums2[n-1] > nums1[m-1] or m == 0:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1

# 测试用例
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
# 测试结果
slu = Solution()
print(nums1,nums2)
slu.merge1(nums1,m,nums2,n)
print('运行结果为',nums1)
