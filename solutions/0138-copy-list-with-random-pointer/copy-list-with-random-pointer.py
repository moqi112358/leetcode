# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#
#
# 	val: an integer representing Node.val
# 	random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
#
#
#  
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
#
# Example 3:
#
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
#
# Example 4:
#
#
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
#
#
#  
# Constraints:
#
#
# 	-10000 <= Node.val <= 10000
# 	Node.random is null or pointing to a node in the linked list.
# 	The number of nodes will not exceed 1000.
#
#


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    # Method 1: use the distance from the end to index random node
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head:
#             return head
#         dummy = Node(0)
#         node_list = []
#         copy = dummy
#         cur = head
#         while cur:
#             copy.next = Node(cur.val)
#             copy = copy.next
#             cur = cur.next
#             tmp = copy
#             node_list.append(tmp)
        
#         cur = head
#         copy = dummy.next
#         while cur:
#             index = self.index(cur.random)
#             if index == -1:
#                 copy.random = None
#             else:
#                 print(index)
#                 copy.random = node_list[-index]
#             copy = copy.next
#             cur = cur.next
#         return dummy.next
    
#     def index(self, node):
#         count = 0
#         if node is None:
#             return -1
#         while node:
#             node = node.next
#             count += 1
#         return count

# Method 2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        while cur:
            tmp = cur.next
            cur.next = Node(cur.val)
            cur.next.next = tmp
            cur = cur.next.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next
        dummy = Node(0)
        node = dummy
        cur = head
        while cur:
            node.next = cur.next
            cur = cur.next.next
            node = node.next
        return dummy.next
