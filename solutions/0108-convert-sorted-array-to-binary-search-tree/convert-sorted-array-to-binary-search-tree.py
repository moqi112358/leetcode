# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            nums.sort()
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        else:
            i, j = 0, len(nums)
            mid = int((i+j)/2)
            root = TreeNode(nums[mid])
            left = self.sortedArrayToBST(nums[0:mid])
            right = self.sortedArrayToBST(nums[mid+1:len(nums)])
            root.left, root.right = left, right
            return root
            
        
        
