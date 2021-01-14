# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
#  
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
#
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
#
#
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
#  
# Constraints:
#
#
# 	The number of nodes in both trees is in the range [0, 100].
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            print(p.val,q.val)
            if p.val != q.val:
                return False
            tmp1 = self.isSameTree(p.left,q.left)
            tmp2 = self.isSameTree(p.right,q.right)
            return tmp1 and tmp2
        elif p is None and q is None:
            return True
        elif p is None or q is None:
            return False
