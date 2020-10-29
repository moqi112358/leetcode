# Given the root of a binary tree, each node in the tree has a distinct value.
#
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
#
# Return the roots of the trees in the remaining forest.  You may return the result in any order.
#
#  
# Example 1:
#
#
#
#
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the given tree is at most 1000.
# 	Each node has a distinct value between 1 and 1000.
# 	to_delete.length <= 1000
# 	to_delete contains distinct values between 1 and 1000.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        queue = [root]
        to_delete = set(to_delete)
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node.val in to_delete:
                if node.left and node.left.val not in to_delete:
                    res.append(node.left)
                else:
                    node.left = None
                if node.right and node.right.val not in to_delete:
                    res.append(node.right)
                else:
                    node.right = None
            else:
                if node.val == root.val:
                    res.append(root)
                if node.left and node.left.val in to_delete:
                    node.left = None
                if node.right and node.right.val in to_delete:
                    node.right = None
        return res
            
            
        
        
