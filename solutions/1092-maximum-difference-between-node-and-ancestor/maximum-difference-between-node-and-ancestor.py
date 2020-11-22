# Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
#
# A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.
#
#  
# Example 1:
#
#
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
#
# Example 2:
#
#
# Input: root = [1,null,2,null,0,3]
# Output: 3
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [2, 5000].
# 	0 <= Node.val <= 105
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxAncestorDiff(self, root: TreeNode) -> int:
    #     res = []
    #     self.searchBinaryTree(root, res)
    #     return max([max(abs(i[0].val - i[1]), abs(i[0].val - i[2])) for i in res])
    # def searchBinaryTree(self, root, res):
    #     if root.left is None and root.right is None:
    #         res.append((root, root.val, root.val))
    #         return root.val, root.val
    #     left_max, right_max = float('-inf'), float('-inf')
    #     left_min, right_min = float('inf'), float('inf')
    #     if root.left:
    #         left_max, left_min = self.searchBinaryTree(root.left, res)
    #     if root.right:
    #         right_max, right_min = self.searchBinaryTree(root.right, res)
    #     node_max = max(left_max, right_max, root.val)
    #     node_min = min(left_min, right_min, root.val)
    #     res.append((root, node_max, node_min))
    #     return node_max, node_min
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.searchBinaryTree(root)
        return self.res
    def searchBinaryTree(self, root):
        if root.left is None and root.right is None:
            self.res = max(self.res, 0)
            return root.val, root.val
        left_max, right_max = float('-inf'), float('-inf')
        left_min, right_min = float('inf'), float('inf')
        if root.left:
            left_max, left_min = self.searchBinaryTree(root.left)
        if root.right:
            right_max, right_min = self.searchBinaryTree(root.right)
        node_max = max(left_max, right_max, root.val)
        node_min = min(left_min, right_min, root.val)
        self.res = max(self.res, abs(root.val - node_max), abs(root.val - node_min))
        return node_max, node_min
        
