/**
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
 */

class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        var map : [Int: Bool] = [:]
        var r = 0

        for el in nums{
            if map[el] != nil{
                map[el] = true
            }else{
                map[el] = false
            }
        }

        for (ind, el) in map{
            if el == false{
                r = ind
            }
        }

        return r
    }
}