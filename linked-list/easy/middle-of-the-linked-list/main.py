# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
#
# If there are two middle nodes, return the second middle node.
#
#
#
# Example 1:
#
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:
#
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.
#
#
# Note:
#
# The number of nodes in the given list will be between 1 and 100.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    size = 0

    def middleNode(self, head: ListNode) -> ListNode:
        i = 0
        node = head

        self.getSize(head)

        while i != self.size // 2:
            node = node.next
            i += 1

        return node

    def getSize(self, node: ListNode) -> None:
        self.size += 1
        if node.next:
            self.getSize(node.next)


# Optimal solution using 2 pointers
class Solution2:

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
