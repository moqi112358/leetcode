# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
#
#
# Example 2:
#
#
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
#
#
# Note:
#
#
# 	The relative order inside both the even and odd groups should remain as it was in the input.
# 	The first node is considered odd, the second node even and so on ...
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # if head is None:
        #     return head
        # dummy = ListNode(0)
        # dummy.next = head
        # even = ListNode(0)
        # dummy_even = even
        # while head.next:
        #     print(head.val, even.val)
        #     even.next = head.next
        #     head.next = head.next.next
        #     even = even.next
        #     if head.next is None:
        #         break
        #     else:
        #         head = head.next
        # even.next = None
        # head.next = dummy_even.next
        # return dummy.next
        if head == None:
            return None 
        
        odd = head
        even_head = head.next
        even = even_head
        
        while (even and even.next):
            
            # Odd values 
            odd.next = even.next
            odd = odd.next
            
            # Even Values
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return head
