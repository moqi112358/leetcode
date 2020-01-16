# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
#
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    #recursion
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = self.traversal(root)
        return l[k-1]
    
    def traversal(self, root):
        if root is None:
            return []
        else:
            return self.traversal(root.left) + [root.val] + self.traversal(root.right)
    '''
    #iteration
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        visited = set()
        stack = [root]
        while stack:
            node = stack[-1]
            if node.left and node.left not in visited:
                stack.append(node.left)
            else:
                out = stack.pop(len(stack) - 1)
                visited.add(out)
                count += 1
                if count == k:
                    return out.val
                if out.right:
                    stack.append(out.right)
        return None
                
        
        
        
