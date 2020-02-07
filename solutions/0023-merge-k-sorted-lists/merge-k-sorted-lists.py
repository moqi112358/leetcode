# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        res = ListNode(0)
        node = res
        k_list = [i.val if i is not None else float("inf") for i in lists ]
        if len(k_list) == 0:
            return None
        while min(k_list) != float("inf"):
            k_min = min(k_list)
            k_index = k_list.index(k_min)
            k_node = lists[k_index]
            node.next = k_node
            node = node.next
            lists[k_index] = lists[k_index].next
            if lists[k_index] is None:
                k_list[k_index] = float("inf")
            else:
                k_list[k_index] = lists[k_index].val
        return res.next
