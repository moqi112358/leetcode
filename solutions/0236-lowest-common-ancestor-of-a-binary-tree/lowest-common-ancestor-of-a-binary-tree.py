# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#  
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
#
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
#
#
# Example 3:
#
#
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [2, 105].
# 	-109 <= Node.val <= 109
# 	All Node.val are unique.
# 	p != q
# 	p and q will exist in the tree.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#     Method1: Ancestor of nodes (nums >= 2): calculate the common prefix
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root:
#             return None
#         res = {}
#         res[''] = root
#         pathSet ={'left':False, 'right':False, 'left_path':'', 'right_path':''}
#         self.dfs(root, res, '', pathSet, p, q)
#         path1, path2 = pathSet['left_path'], pathSet['right_path']
#         path = ''
#         l = min(len(path1), len(path2))
#         for i in range(l):
#             if path1[i] == path2[i]:
#                 path += path1[i]
#             else:
#                 break
#         if path in res:
#             return res[path]
#         return root
    
#     def dfs(self, node, res, path, pathSet, p, q):
#         res[path] = node
#         if node.val == p.val:
#             pathSet['left'] = True
#             pathSet['left_path'] = path
#         if node.val == q.val:
#             pathSet['right'] = True
#             pathSet['right_path'] = path
#         if pathSet['left'] and pathSet['right']:
#             return
#         if node.left:
#             self.dfs(node.left, res, path+'l', pathSet, p, q)
#         if node.right:
#             self.dfs(node.right, res, path+'r', pathSet, p, q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':     
        res = set()
        parent = {root:''}
        queue = [root]
        while p not in parent or q not in parent:
            node = queue.pop(0)
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                parent[node.right] = node
        
        while p in parent:
            res.add(p)
            p = parent[p]
        
        while q not in res:
            q = parent[q]
        return q
