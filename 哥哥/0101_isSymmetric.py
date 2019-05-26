# -*- coding: utf-8 -*-
"""
时间：2019-05-26
作者：哥哥
题号：0101

题目：
给定一个二叉树，检查它是否是镜像对称的。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    # 递归判断
    def isSymmetric1(self, root):
        # 递归核
        def isSymmetricCore(left, right):
            # 左右子树均为空
            if not left and not right:
                return True
            # 左右子树均不为空
            if left and right:
                return (left.val == right.val and isSymmetricCore(left.left,right.right)
                        and isSymmetricCore(left.right,right.left))
            else:
                return False
        
        # 若树不为空
        if root:
            return isSymmetricCore(root.left,root.right)
        else:
            return True
            
    # 迭代判断
    def isSymmetric2(self, root):
        # 当前层节点
        queue = [root]
        while(queue):
            # 下一层节点
            next_queue = []
            # 当前层节点值
            layer = []
            for node in queue:
                if not node:
                    layer.append(node)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)
                layer.append(node.val)
            # 判断当前层节点值列表是否为回文列表
            if layer != layer[::-1]:
                return False
            # 下一层节点替换当前层节点
            queue = next_queue
        return True

# 测试用例
testNode1 = TreeNode(1)
testNode2 = TreeNode(2)
testNode3 = TreeNode(2)
testNode4 = TreeNode(3)
testNode5 = TreeNode(4)
testNode6 = TreeNode(4)
testNode7 = TreeNode(3)
testNode1.left = testNode2
testNode1.right = testNode3
testNode2.left = testNode4
testNode2.right = testNode5
testNode3.left = testNode6
testNode3.right = testNode7
# 测试结果
slu = Solution()
print(slu.isSymmetric1(testNode1))
print(slu.isSymmetric2(testNode1))
