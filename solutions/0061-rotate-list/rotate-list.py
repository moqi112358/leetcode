# Given the head of a linked list, rotate the list to the right by k places.
#
#  
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
#
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is in the range [0, 500].
# 	-100 <= Node.val <= 100
# 	0 <= k <= 2 * 109
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        k = k % l
        if k == 0:
            return head
        cur = head
        t = l - k
        while t > 0:
            t -= 1
            tmp = cur.next
            if t == 0:
                cur.next = None
            cur = tmp
        res = cur
        while cur.next:
            cur = cur.next
        cur.next = head
        return res
