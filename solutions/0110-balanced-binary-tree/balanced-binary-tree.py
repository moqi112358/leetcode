# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
#
#  
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#
#
# Return false.
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
