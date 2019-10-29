# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        self.res = []
        self.helper(root, '')
        return list(set(self.res))
    def helper(self, root, path):
        if root and (root.left or root.right):
            if root.left:
                self.helper(root.left,path+str(root.val)+'->')
            if root.right:
                self.helper(root.right,path+str(root.val)+'->')
        else:
            path += str(root.val)
            self.res.append(path)
