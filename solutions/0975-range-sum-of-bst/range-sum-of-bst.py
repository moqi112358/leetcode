# -*- coding:utf-8 -*-


# Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
#
#  
# Example 1:
#
#
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
#
#
# Example 2:
#
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [1, 2 * 104].
# 	1 <= Node.val <= 105
# 	1 <= low <= high <= 105
# 	All Node.val are unique.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        queue = [root]
        while queue:
            node = queue.pop(0)
            if L <= node.val <= R:
                res += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
        
        
