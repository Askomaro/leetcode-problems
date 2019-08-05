# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".
#
# Example 1:
#
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:
#
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"


# simplest approach
def approach1(address):
    result = ''
    for el in address:
        if el == '.':
            result += '[.]'
        else:
            result += el

    return result


def approach2(address):
    return '[.]'.join(address.split('.'))


if __name__ == '__main__':
    assert approach1("255.100.50.0") == "255[.]100[.]50[.]0"
    assert approach1("1.1.1.1") == "1[.]1[.]1[.]1"

    assert approach2("255.100.50.0") == "255[.]100[.]50[.]0"
    assert approach2("1.1.1.1") == "1[.]1[.]1[.]1"

