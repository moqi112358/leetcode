# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins.
#
#  
#
# Example 1:
#
#
#
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#
#
#
# Example 2:
#
#
#
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
#
#
#
# Example 3:
#
#
#
#
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
#
#
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree will be between 2 and 100.
# 	Each node has a unique integer value from 1 to 100.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depth_x, depth_y = -1, -1
        root_x, root_y = None, None
        queue = [root]
        level = 0
        while queue:
            tmp_queue = []
            for pre_node in queue:
                if pre_node.left:
                    tmp_queue.append(pre_node.left)
                    if pre_node.left.val == x:
                        root_x = pre_node.val
                        depth_x = level + 1
                    if pre_node.left.val == y:
                        root_y = pre_node.val
                        depth_y = level + 1
                if pre_node.right:
                    tmp_queue.append(pre_node.right)
                    if pre_node.right.val == x:
                        root_x = pre_node.val
                        depth_x = level + 1
                    if pre_node.right.val == y:
                        root_y = pre_node.val
                        depth_y = level + 1
            level += 1
            queue = tmp_queue.copy()
        return depth_x == depth_y and root_x != root_y
        
