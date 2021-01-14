# -*- coding:utf-8 -*-


# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
#
#  
# Example 1:
#
#
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
#
#
# Example 2:
#
#
# Input: root = [4,2,7,1,3], val = 5
# Output: []
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [1, 5000].
# 	1 <= Node.val <= 107
# 	root is a binary search tree.
# 	1 <= val <= 107
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        elif root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
