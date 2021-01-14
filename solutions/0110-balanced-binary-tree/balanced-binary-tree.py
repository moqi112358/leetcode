# -*- coding:utf-8 -*-


# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
# Example 3:
#
#
# Input: root = []
# Output: true
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 5000].
# 	-104 <= Node.val <= 104
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res, _ = self.helper(root)
        return res
    
    def helper(self, root):
        if root is None:
            return True, 0
        else:
            b1, d1 = self.helper(root.left)
            b2, d2 = self.helper(root.right)
            return b1 and b2 and abs(d1 - d2) <= 1, max(d1, d2) + 1
