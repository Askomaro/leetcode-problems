/**
 The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
 */

class Solution {
    func mergeTrees(_ t1: TreeNode?, _ t2: TreeNode?) -> TreeNode? {
        if t1 == nil {
            return t2
        }

        if t2 == nil {
            return t1
        }
        t1!.val += t2!.val
        t1!.left = mergeTrees(t1?.left, t2?.left)
        t1!.right = mergeTrees(t1?.right, t2?.right)

        return t1
    }

    func hammingDistance2(_ x: Int, _ y: Int) -> Int {
        return (x ^ y).nonzeroBitCount
    }
}