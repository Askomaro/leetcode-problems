/**
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
 */

class Solution {
    func strStr(_ haystack: String, _ needle: String) -> Int {
        if needle.isEmpty{
            return 0
        }

        let haystackChars = Array(haystack)
        let needleChars = Array(needle)
        var i = 0
        var j = 0

        while i < haystackChars.count{
            if haystackChars[i] == needleChars[j]{
                j += 1

                if j == needleChars.count{
                    return i - j + 1
                }
            } else{
                i -= j
                j = 0
            }

            i += 1
        }

        return -1
    }
}