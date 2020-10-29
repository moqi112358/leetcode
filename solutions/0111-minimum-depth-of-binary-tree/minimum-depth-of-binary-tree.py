# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#
#
# Example 2:
#
#
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 105].
# 	-1000 <= Node.val <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            if left == 0 or right == 0:
                return 1 + left + right
            else:
                return min(left, right) + 1
        
