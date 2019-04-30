# -*- coding: utf-8 -*-
"""
时间：2019-04-28
作者：哥哥
题号：0021

题目：
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    # 方法1 双循环处理
    def mergeTwoLists1(self, l1, l2):
        # 特殊处理，其中一个链表为空，直接返回另一个链表
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # 根节点
        root = ListNode(None)
        node = root
        # 循环添加节点
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        # 剩余处理
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        # 返回
        return root.next

    #方法2 递归处理
    def mergeTwoLists2(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2

