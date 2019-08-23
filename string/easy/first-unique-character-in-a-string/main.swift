/**
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

*/

class Solution {
    func firstUniqChar(_ s: String) -> Int {
        var dict : [Character:Int] = [:]

        for el in s{
            if dict[el] == nil{
                dict[el] = 1
            }else{
                dict[el]! += 1
            }
        }

        for (ind, el) in s.enumerated(){
            if dict[el] == 1 {
                return ind
            }
        }

        return -1
    }
}