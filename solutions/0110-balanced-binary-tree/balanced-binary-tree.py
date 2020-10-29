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
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        res, _ = self.maxDepth(root)
        return res
        
    def maxDepth(self, root):
        if root is None:
            return True, 0
        else:
            left, left_depth = self.maxDepth(root.left)
            right, right_depth = self.maxDepth(root.right)
            tmp = abs(left_depth - right_depth)
            return left and right and tmp <= 1, max(left_depth, right_depth) + 1
