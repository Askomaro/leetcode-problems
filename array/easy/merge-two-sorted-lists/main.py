# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
# the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ft = True
        while True:
            if ft:
                ft = False
                if l1.val >= l2.val:
                    result = l2
                    l2 = l2.next
                    continue
                else:
                    result = l1
                    l1 = l1.next
                    continue

            if l1.next == None and l2.next != None:
                result.next = l2
                break

            if l1.next != None and l2.next == None:
                result.next = l1
                break

            if l1.val >= l2.val:
                result.next = l2
                l2 = l2.next
            else:
                result.next = l1
                l1 = l1.next

            if l1.next == None and l2.next == None:
                break

        return result
