# Sort a linked list using insertion sort.
#
#
#
#
#
# A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
#  
#
#
#
#
# Algorithm of Insertion Sort:
#
#
# 	Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# 	At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# 	It repeats until no input elements remain.
#
#
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#         res = ListNode(float('-inf'))
#         while head:
#             res = self.inserNode(res, head.val)
#             head = head.next
#         return res.next
    
#     def inserNode(self, res, nodeVal):
#         cur = res
#         while cur:
#             if cur.next is None:
#                 cur.next = ListNode(nodeVal)
#                 break
#             if nodeVal <= cur.next.val:
#                 node = ListNode(nodeVal, cur.next)
#                 cur.next = node
#                 break
#             else:
#                 cur = cur.next
#         return res
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy=ListNode(-1,head)
        cur=head
        prev,temp=None,None
        while cur and cur.next:
            if cur.val <= cur.next.val:
                cur=cur.next
            else:
                temp=cur.next
                cur.next=cur.next.next
                prev=dummy
                while prev.next.val <= temp.val:
                    prev=prev.next
                temp.next=prev.next
                prev.next=temp
        return dummy.next
            
