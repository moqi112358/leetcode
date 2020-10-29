# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
#
# Return the following binary tree:
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         if len(inorder) == 0 or len(postorder) == 0:
#             return None
#         root_val = postorder.pop()
#         root = TreeNode(root_val)
#         root_inorder_index = inorder.index(root_val)
#         left_inorder, right_inorder = inorder[:root_inorder_index], inorder[root_inorder_index+1:]
#         left_postorder, right_postorder = postorder[:len(left_inorder)], postorder[len(left_inorder):]
#         root = TreeNode(root_val)
#         root.left = self.buildTree(left_inorder, left_postorder)
#         root.right = self.buildTree(right_inorder, right_postorder)
#         return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return
        indices = {inorder[i]:i for i in range(len(inorder))}
        def dfs(l,r):
            if l > r:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            
            val_index = indices[val]
            root.right = dfs(val_index+1,r)
            root.left = dfs(l,val_index-1)
            
            return root
            
            
            
        return dfs(0,len(inorder)-1)
