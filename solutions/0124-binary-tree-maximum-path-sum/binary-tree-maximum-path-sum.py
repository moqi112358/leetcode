# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any path.
#
#  
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
#
#
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [1, 3 * 104].
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
#     def maxPathSum(self, root: TreeNode) -> int:
#         self.res = float('-inf')
#         if root is None:
#             return None
#         self.helper(root)
#         return self.res
    
#     def helper(self, node):
#         if node is None:
#             return float('-inf'),  float('-inf')
#         left, right =  float('-inf'),  float('-inf')
#         left_node_left, left_node_right = float('-inf'),  float('-inf')
#         right_node_left, right_node_right = float('-inf'),  float('-inf')
#         if node.left:
#             left_node_left, left_node_right = self.helper(node.left)
#         if node.right:
#             right_node_left, right_node_right = self.helper(node.right)
#         #left path
#         left = max(node.val, node.val + left_node_left, node.val + left_node_right )
#         right = max(node.val, node.val + right_node_left, node.val + right_node_right )
#         # Maximum Path Sum through node and its ancestor not included
#         m = max(node.val, left, right, left + right - node.val)
#         self.res = max(m, self.res)
#         return left, right
#     def maxPathSum(self, root: TreeNode) -> int:
#         self.res = float('-inf')
#         self.helper(root)
#         return self.res
    
#     def helper(self, root):
#         if root is None:
#             return 0
#         left, right = self.helper(root.left), self.helper(root.right)
#         self.res = max(root.val + max(0, left) + max(0, right), self.res)
#         return root.val + max(left, right, 0)
    def __init__(self):
        self.maxVal = 0
    def getSum(self, root):
        if not root:
            return 0
        left = max(0, self.getSum(root.left))
        right = max(0, self.getSum(root.right))
        
        self.maxVal = max(self.maxVal, root.val+left+right )
        
        return max(left, right) + root.val
    
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maxVal = root.val
        self.getSum(root)
        return self.maxVal
        
