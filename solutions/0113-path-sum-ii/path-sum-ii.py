# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
#
#
# Return:
#
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, total_sum: int) -> List[List[int]]:
        res = []
        self.helper(root, [], res, 0, total_sum)
        return res
    
    def helper(self, node, path, res, s, total_sum):
        if node is None:
            return
        if node.left is None and node.right is None:
            if s + node.val == total_sum:
                res.append(path + [node.val])
                return
            else:
                return
        if node.left:
            self.helper(node.left, path+[node.val], res, s+node.val, total_sum)
        if node.right:
            self.helper(node.right, path+[node.val], res, s+node.val, total_sum)
        
