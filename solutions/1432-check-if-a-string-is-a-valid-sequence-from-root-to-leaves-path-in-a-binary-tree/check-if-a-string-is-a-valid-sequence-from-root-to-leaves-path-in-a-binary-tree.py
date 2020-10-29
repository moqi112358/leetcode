# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 
#
# We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
#
#  
# Example 1:
#
#
#
#
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation: 
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
# Other valid sequences are: 
# 0 -> 1 -> 1 -> 0 
# 0 -> 0 -> 0
#
#
# Example 2:
#
#
#
#
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
# Output: false 
# Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
#
#
# Example 3:
#
#
#
#
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
# Output: false
# Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.
#
#
#  
# Constraints:
#
#
# 	1 <= arr.length <= 5000
# 	0 <= arr[i] <= 9
# 	Each node's value is between [0 - 9].
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root or root.val != arr[0]:
            return False
        else:
            return self.dfs(root, arr[1:])
    
    def dfs(self, root, arr):
        if root.right is None and root.left is None and len(arr) == 0:
            return True
        elif root.right is None and root.left is None and len(arr) != 0:
            return False
        elif not (root.right is None and root.left is None) and len(arr) == 0:
            return False
        else:
            if root.left and root.left.val == arr[0]:
                left = self.dfs(root.left, arr[1:])
                if left:
                    return True
            if root.right and root.right.val == arr[0]:
                right = self.dfs(root.right, arr[1:])
                if right:
                    return True
            return False
        
