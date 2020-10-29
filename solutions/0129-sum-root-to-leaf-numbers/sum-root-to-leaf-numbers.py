# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
# Example 2:
#
#
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def sumNumbers(self, root: TreeNode) -> int:
#         res = self.helper(root)
#         if len(res) == 0:
#             return 0
#         else:
#             return sum([int(num) for num in res])
    
#     def helper(self, root):
#         if root is None:
#             return []
#         left_list = self.helper(root.left)
#         right_list = self.helper(root.right)
#         if len(left_list) == 0 and len(right_list) == 0:
#             return [str(root.val)]
#         res = []
#         for num in left_list:
#             res.append(str(root.val)+num)
#         for num in right_list:
#             res.append(str(root.val)+num)
#         return res

    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = []
        self.helper(root, 0, res)
        return sum(res)

    def helper(self, root, num, res):
        if root.left is None and root.right is None:
            res.append(num * 10 + root.val)
        if root.left:
            self.helper(root.left, num * 10 + root.val, res)
        if root.right:
            self.helper(root.right, num * 10 + root.val, res)
        
        
        
        
