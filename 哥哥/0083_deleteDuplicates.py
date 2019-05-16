# -*- coding: utf-8 -*-
"""
时间：2019-05-10
作者：哥哥
题号：0083

题目：
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    def deleteDuplicates(self, head):
        nowNode = head
        while nowNode and nowNode.next:
            nextNode = nowNode.next
            if nowNode.val == nextNode.val:
                nowNode.next = nextNode.next
            else:
                nowNode = nextNode
        return head
