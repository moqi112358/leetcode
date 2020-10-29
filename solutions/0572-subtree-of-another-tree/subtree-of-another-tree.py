# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
#
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#
# Given tree t:
#
#
#    4 
#   / \
#  1   2
#
# Return true, because t has the same structure and node values with a subtree of s.
#
#  
#
# Example 2:
# Given tree s:
#
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#
# Given tree t:
#
#
#    4
#   / \
#  1   2
#
# Return false.
#
#  
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # Method1: O(|s||t|)
        queue = [s]
        res = False
        while queue:
            node = queue.pop(0)
            if node.val == t.val:
                res = res or (self.check(node, t))
            if res:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
        
        
    def check(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        return node1.val == node2.val and self.check(node1.left, node2.left) and self.check(node1.right, node2.right)
        
    # Method2: convert to str and use str1.find(str2) O(|S| + |T|)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
        
        return convert(t) in convert(s)
