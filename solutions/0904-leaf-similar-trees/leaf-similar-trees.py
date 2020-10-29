# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
#  
# Example 1:
#
#
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
#
# Example 2:
#
#
# Input: root1 = [1], root2 = [1]
# Output: true
#
#
# Example 3:
#
#
# Input: root1 = [1], root2 = [2]
# Output: false
#
#
# Example 4:
#
#
# Input: root1 = [1,2], root2 = [2,2]
# Output: true
#
#
# Example 5:
#
#
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
#
#  
# Constraints:
#
#
# 	The number of nodes in each tree will be in the range [1, 200].
# 	Both of the given trees will have values in the range [0, 200].
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        tmp1 = self.leaf(root1)
        tmp2 = self.leaf(root2)
        return tmp1 == tmp2
    def leaf(self, root):
        res = []
        if root.left is None and root.right is None:
            return [root.val]
        if root.left:
            res.extend(self.leaf(root.left))
        if root.right:
            res.extend(self.leaf(root.right))
        return res
