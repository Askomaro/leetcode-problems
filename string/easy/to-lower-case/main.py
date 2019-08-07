# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
# Example 1:
# Input: "Hello"
# Output: "hello"

# Example 2:
# Input: "here"
# Output: "here"

# Example 3:
# Input: "LOVELY"
# Output: "lovely"


def approach1(in_str):
    return ''.join([el if ord(el) > 96 or ord(el) < 65 else chr(ord(el) + 32) for el in in_str])


if __name__ == '__main__':
    assert approach1("Hello") == "hello"
    assert approach1("here") == "here"
    assert approach1("LOVELY") == "lovely"
    assert approach1("al&phaBET") == "al&phabet"


