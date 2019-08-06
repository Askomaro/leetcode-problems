# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
# so "a" is considered a different type of stone from "A".
#
# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# Example 2:
# Input: J = "z", S = "ZZ"
# Output: 0


def approach1(J, S):
    count = 0
    if len(S) == 0:
        return count

    for myStone in S:
        for jewel in J:
            if jewel in myStone:
                count += 1

    return count


def approach2(J, S):
    count = 0
    if len(S) == 0:
        return count
    
    return len([char for char in S if char in J])


if __name__ == '__main__':
    assert approach1("aA", "aAAbbbb") == 3
    assert approach1("z", "ZZ") == 0

    assert approach2("aA", "aAAbbbb") == 3
    assert approach2("z", "ZZ") == 0
