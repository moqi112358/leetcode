# Given the root of a binary tree and a node u in the tree, return the nearest node on the same level that is to the right of u, or return null if u is the rightmost node in its level.
#
#  
# Example 1:
#
#
#
#
# Input: root = [1,2,3,null,4,5,6], u = 4
# Output: 5
# Explanation: The nearest node on the same level to the right of node 4 is node 5.
#
#
# Example 2:
#
#
#
#
# Input: root = [3,null,4,2], u = 2
# Output: null
# Explanation: There are no nodes to the right of 2.
#
#
# Example 3:
#
#
# Input: root = [1], u = 1
# Output: null
#
#
# Example 4:
#
#
# Input: root = [3,4,2,null,null,null,1], u = 4
# Output: 2
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [1, 105].
# 	1 <= Node.val <= 105
# 	All values in the tree are distinct.
# 	u is a node in the binary tree rooted at root.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
#         queue = [root]
#         while queue:
#             if u in queue:
#                 index = queue.index(u)
#                 if index == len(queue) - 1:
#                     return None
#                 else:
#                     return queue[index+1]
#             tmp = []
#             for node in queue:
#                 if node.left:
#                     tmp.append(node.left)
#                 if node.right:
#                     tmp.append(node.right)
#             queue = tmp
#         return None
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        queue = deque([root, None,])      
        while queue:
            curr = queue.popleft()
            
            # if it's the given node
            if curr == u:
                return queue.popleft()
            
            if curr:
                # add child nodes in the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            else:
                # once the level is finished,
                # add a sentinel to mark end of level
                if queue:
                    queue.append(None)
