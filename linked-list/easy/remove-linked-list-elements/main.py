# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # Use dummy head.  This works because objects are pointers to heap memory locations.
        # p moves but dum stays pointed at original memory location.
        node = head
        p = dum = ListNode(None)

        while node:
            if node.val == val:
                node = node.next
                p.next = None
            else:
                p.next = node
                node = node.next
                p = p.next

        return dum.next
