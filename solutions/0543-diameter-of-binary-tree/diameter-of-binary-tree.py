#
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
#
#
# Example:
# Given a binary tree 
#
#           1
#          / \
#         2   3
#        / \     
#       4   5    
#
#
#
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
#
# Note:
# The length of path between two nodes is represented by the number of edges between them.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        _, res = self.helper(root)
        return max(0, res - 1)
    
    def helper(self, root):
        if root is None:
            return 0, 0
        else:
            l, res_l = self.helper(root.left)
            r, res_r = self.helper(root.right)
            return max(l, r) + 1, max(res_l, res_r, l + r + 1)
