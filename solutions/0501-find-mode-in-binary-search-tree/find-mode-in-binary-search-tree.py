# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
#
# Assume a BST is defined as follows:
#
#
# 	The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# 	The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# 	Both the left and right subtrees must also be binary search trees.
#
#
#  
#
# For example:
# Given BST [1,null,2,2],
#
#
#    1
#     \
#      2
#     /
#    2
#
#
#  
#
# return [2].
#
# Note: If a tree has more than one mode, you can return them in any order.
#
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
#


#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (40.48%)
# Total Accepted:    67.6K
# Total Submissions: 167K
# Testcase Example:  '[1,null,2,2]'
#
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the
# most frequently occurred element) in the given BST.
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# For example:
# Given BST [1,null,2,2],
# 
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
# 
# 
# 
# 
# return [2].
# 
# Note: If a tree has more than one mode, you can return them in any order.
# 
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res = self.helper(root)
        if len(res) == 0:
            return []
        hc = {}
        for i in res:
            hc[i] = hc.get(i, 0) + 1
        mode_c = max(list(hc.values()))
        res = []
        for i in hc:
            if hc[i] == mode_c:
                res.append(i)
        return res



    def helper(self, root):
        if root is None:
            return []
        else:
            return self.helper(root.left) +[root.val] + self.helper(root.right)


