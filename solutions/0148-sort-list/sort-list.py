# Sort a linked list in O(n log n) time using constant space complexity.
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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        first = head
        second = slow.next
        slow.next = None
        left, right = self.sortList(first), self.sortList(second)
        return self.merge(left, right)
    
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        dummy = ListNode(0)
        node = dummy
        while left and right:
            if left.val > right.val:
                node.next = right
                right = right.next
                node = node.next
            else:
                node.next = left
                left = left.next
                node = node.next
        if left:
            node.next = left
        elif right:
            node.next = right
        return dummy.next
        
