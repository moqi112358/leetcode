# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
#
# 	The left subtree of a node contains only nodes with keys less than the node's key.
# 	The right subtree of a node contains only nodes with keys greater than the node's key.
# 	Both the left and right subtrees must also be binary search trees.
#
#
#  
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [1, 104].
# 	-231 <= Node.val <= 231 - 1
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res, min_tree, max_tree = self.helper(root)
        print(min_tree, max_tree)
        return res
    
    def helper(self, root):
        if root is None:
            return True, -1 * float('inf'), float('inf')
        left_bool, left_max, left_min = self.helper(root.left)
        right_bool, right_max, right_min = self.helper(root.right)
        if left_bool and right_bool and root.val > left_max and root.val < right_min:
            min_tree = root.val if left_min == float('inf') else left_min
            max_tree = root.val if right_max == -1 * float('inf') else right_max
            return True, max_tree, min_tree
        else:
            return False, root.val, root.val
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        # top down with pre-order traverse
        return self.pre_order(root, -float('inf'), float('inf'))
        
    def pre_order(self, root, left, right) -> bool:
        if not root:
            return True
        if not (left < root.val < right):
            return False
        return self.pre_order(root.left, left, root.val) and self.pre_order(root.right, root.val, right)
    '''
        
