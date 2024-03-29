# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    sum_leafs = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return self.sum_leafs

        self.isLeftLeaf(root.left, True)
        self.isLeftLeaf(root.right, False)

        return self.sum_leafs

    def isLeftLeaf(self, root, is_left):
        if not root:
            return

        if not root.left and not root.right and is_left:
            self.sum_leafs += root.val
            return

        self.isLeftLeaf(root.left, True)
        self.isLeftLeaf(root.right, False)
