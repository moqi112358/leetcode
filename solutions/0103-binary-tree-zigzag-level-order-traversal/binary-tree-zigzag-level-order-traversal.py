# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its zigzag level order traversal as:
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        queue = [root]
        left2right = False
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if tmp:
                if left2right:
                    res.append([i.val for i in tmp])
                    left2right = False
                elif not left2right:
                    res.append([i.val for i in tmp[::-1]])
                    left2right = True
            queue = tmp
        return res
            
            
        
