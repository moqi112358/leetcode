# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = 0
        queue = [(root, 'root')]
        while queue:
            node, node_type = queue.pop(0)
            if node.left is None and node.right is None and node_type == 'left':
                res += node.val
            if node.left:
                queue.append((node.left, 'left'))
            if node.right:
                queue.append((node.right, 'right'))
        return res
        
