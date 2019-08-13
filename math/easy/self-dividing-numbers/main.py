# A self-dividing number is a number that is divisible by every digit it contains. #
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0. #
# Also, a self-dividing number is not allowed to contain the digit zero. #
# Given a lower and upper number bound, output a list of every possible self dividing number,
# including the bounds if possible. #

# Example 1:
# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

# Note: #
# The boundaries of each input argument are 1 <= left <= right <= 10000.


def approach1(left, right):
    result = []
    for num in range(left, right + 1):
        flag = False
        for ch in str(num):
            if ch == '0' or num % int(ch) != 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            result.append(num)

    return result


def approach2(left, right):
    return [number for number in range(left, right + 1) if
            '0' not in str(number) and all((number % int(char) == 0 for char in str(number)))]


if __name__ == '__main__':
    assert approach1(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert approach2(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
