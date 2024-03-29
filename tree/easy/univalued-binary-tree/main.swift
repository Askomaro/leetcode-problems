/**
 A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.



Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false


Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].


 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

class Solution {
    var st : Set<Int> = []

    func isUnivalTree(_ root: TreeNode?) -> Bool {
        let vr = root!.val
        helper(root)
        return st.count == 1
    }

    func helper(_ root: TreeNode?) {
        if root != nil {
            self.helper(root!.left)
            self.helper(root!.right)
            self.st.insert(root!.val)
        }
    }
}