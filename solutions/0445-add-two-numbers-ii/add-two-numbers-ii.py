# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
#
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.list2num(l1)
        num2 = self.list2num(l2)
        num = num1 + num2
        res = self.num2list(num)
        return res

    def list2num(self, l):
        s = ''
        while l:
            s += str(l.val)
            l = l.next
        return int(s)
    
    def num2list(self, num):
        res = ListNode(0)
        cur = res
        s = str(num)
        for i in s:
            cur.next = ListNode(int(i))
            cur = cur.next
        return res.next
