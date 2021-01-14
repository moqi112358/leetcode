# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
#
# Example 1:
#
#
# Input: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
#
# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
# Example 2:
#
#
# Input: [3,4,5,1,3,null,1]
#
#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
#
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def rob(self, root: TreeNode) -> int:
#         return max(self.dp(root, True), self.dp(root, False))
    
#     def dp(self, root, state):
#         if root is None:
#             return 0 
#         if state:
#             left_val = self.dp(root.left, False)
#             right_val = self.dp(root.right, False)
#             return root.val + left_val + right_val
#         elif not state:
#             left_val = max(self.dp(root.left, True), self.dp(root.left, False))
#             right_val = max(self.dp(root.right, True), self.dp(root.right, False))
#             return left_val + right_val


#     def rob(self, root: TreeNode) -> int:
#         if not root:
#             return 0
            
#         # reform tree into array-based tree
#         tree = []
#         graph = {-1: []}
#         index = -1
#         q = [(root, -1)]
#         while q:
#             node, parent_index = q.pop(0)
#             if node:
#                 index += 1
#                 tree.append(node.val)
#                 graph[index] = []
#                 graph[parent_index].append(index)
#                 q.append((node.left, index))
#                 q.append((node.right, index))
#         # represent the maximum start by node i with robbing i
#         dp_rob = [0] * (index + 1)
#         # represent the maximum start by node i without robbing i
#         dp_not_rob = [0] * (index + 1)
#         for i in range(index, -1, -1):
#             if len(graph[i]) == 0:
#                 dp_rob[i] = tree[i]
#                 dp_not_rob[i] = 0
#             else:
#                 dp_rob[i] = tree[i] + sum(dp_not_rob[child] for child in graph[i])
#                 dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child]) for child in graph[i])
#         return max(dp_rob[0], dp_not_rob[0])

    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))
    
    # return max value from below using root and not using root
    def helper(self, root):
        if root:
            left_not_Include, left_Include = self.helper(root.left)
            right_not_Include, right_Include = self.helper(root.right)
            leftRightNotIncluded = root.val + left_not_Include + right_not_Include
            leftRightMaybeIncluded = max(left_not_Include, left_Include) + max(right_not_Include, right_Include)
            return leftRightMaybeIncluded, leftRightNotIncluded
        return 0, 0
        
