/**
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

class Solution {
    // O(n^2); O(1)
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var s = 0
        var e = 0

        for i in 0..<nums.count{
            for j in i+1..<nums.count{
                if nums[i] + nums[j] == target{
                    s = i
                    e = j
                    break
                }
            }

        }

        return [s, e]
    }

    // O(n); O(m)
    func twoSum2(_ nums: [Int], _ target: Int) -> [Int] {
        var s = 0
        var e = 0
        var map : [Int: Int] = [:]

        for i in 0..<nums.count{
            var temp = target - nums[i]
            if let val = map[temp] {
                s = val
                e = i
            }
            map[nums[i]] = i
        }

        return [s, e]
    }
}