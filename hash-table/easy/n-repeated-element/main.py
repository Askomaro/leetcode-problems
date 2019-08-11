# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#
# Return the element repeated N times.
#
#
#
# Example 1:
# Input: [1,2,3,3]
# Output: 3

# Example 2:
# Input: [2,1,2,5,3,2]
# Output: 2

# Example 3:
# Input: [5,1,5,2,5,3,5,4]
# Output: 5


def approach1(A):
    cache = {}

    for el in A:
        if el in cache:
            return el
        else:
            cache[el] = 0


if __name__ == '__main__':
    assert approach1([1,2,3,3]) == 3
    assert approach1([2,1,2,5,3,2]) == 2
    assert approach1([5,1,5,2,5,3,5,4]) == 5

