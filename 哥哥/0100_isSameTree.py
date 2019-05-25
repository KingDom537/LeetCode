# -*- coding: utf-8 -*-
"""
时间：2019-05-25
作者：哥哥
题号：0100

题目：
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    
    # 第一遍写
    def isSameTree1(self, p, q):
        # 空节点
        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        # 当前节点值不同
        if p.val != q.val:
            return False
        # 当前节点值相同
        else:
            # 当前节点结构不同
            if((p.left == None and q.left != None) or (p.left != None and q.left == None) or
               (p.right == None and q.right != None) or (p.right != None and q.right == None)):
                return False
            # 当前节点左子树不同
            if p.left != None and q.left != None:
                if not self.isSameTree(p.left,q.left):
                    return False
            # 当前节点右子树不同
            if p.right != None and q.right != None:
                if not self.isSameTree(p.right,q.right):
                    return False
            return True
        
    # 代码简化
    def isSameTree2(self, p, q):
        # 均为空节点
        if not p and not q:
            return True
        # 均不为空节点
        if p and q:
            return p.val == q.val and self.isSameTree2(p.left,q.left) and self.isSameTree2(p.right,q.right)
        else:
            return False
        
# 测试用例
testNode1 = TreeNode(1)
testNode2 = TreeNode(2)
testNode3 = TreeNode(3)
testNode4 = TreeNode(1)
testNode5 = TreeNode(2)
testNode6 = TreeNode(3)
testNode1.left = testNode2
testNode1.right = testNode3
testNode4.left = testNode5
testNode4.right = testNode6
# 测试结果
slu = Solution()
print(slu.isSameTree2(testNode1,testNode4))
