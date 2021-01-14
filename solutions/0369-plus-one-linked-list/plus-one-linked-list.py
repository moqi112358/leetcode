# Given a non-negative integer represented as a linked list of digits, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list.
#
#  
# Example 1:
# Input: head = [1,2,3]
# Output: [1,2,4]
# Example 2:
# Input: head = [0]
# Output: [1]
#
#  
# Constraints:
#
#
# 	The number of nodes in the linked list is in the range [1, 100].
# 	0 <= Node.val <= 9
# 	The number represented by the linked list does not contain leading zeros except for the zero itself. 
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        rev_head = self.reverse(head)
        flag = 1
        cur = rev_head
        while cur:
            cur.val = cur.val + flag
            if cur.val >= 10:
                cur.val -= 10
                flag = 1
            else:
                flag = 0
            cur = cur.next
        res = self.reverse(rev_head)
        if flag == 1:
            res = ListNode(1, res)
        return res
    
    def reverse(self, head):
        res = None
        while head:
            tmp = head.next
            head.next = res
            res = head
            head = tmp
        return res
