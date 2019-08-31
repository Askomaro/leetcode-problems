# Given a word, you need to judge whether the usage of capitals in it is right or not.
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.
#
#
# Example 1:
#
# Input: "USA"
# Output: True
#
#
# Example 2:
#
# Input: "FlaG"
# Output: False
#
#
# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.


def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    first_capital = True if ord(word[0]) < 97 else False
    all_capital, only_first_capital, all_not_capital = first_capital, first_capital, not first_capital

    for el in word[1:]:
        if ord(el) < 96:
            only_first_capital = False
            all_not_capital = False
        elif ord(el) > 96:
            all_capital = False

    return all_capital or all_not_capital or only_first_capital


if __name__ == '__main__':
    assert detectCapitalUse("USA") == True
    assert detectCapitalUse("FlaG") == False
