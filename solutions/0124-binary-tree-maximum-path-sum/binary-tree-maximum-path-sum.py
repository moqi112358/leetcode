# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# Example 1:
#
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
#
#
# Example 2:
#
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        if root is None:
            return None
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if node is None:
            return float('-inf'),  float('-inf')
        left, right =  float('-inf'),  float('-inf')
        left_node_left, left_node_right = float('-inf'),  float('-inf')
        right_node_left, right_node_right = float('-inf'),  float('-inf')
        if node.left:
            left_node_left, left_node_right = self.helper(node.left)
        if node.right:
            right_node_left, right_node_right = self.helper(node.right)
        #left path
        left = max(node.val, node.val + left_node_left, node.val + left_node_right )
        right = max(node.val, node.val + right_node_left, node.val + right_node_right )
        # Maximum Path Sum through node and its ancestor not included
        m = max(node.val, left, right, left + right - node.val)
        self.res = max(m, self.res)
        return left, right
 
        
