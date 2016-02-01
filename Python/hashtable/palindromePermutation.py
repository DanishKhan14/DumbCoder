"""
Count the frequency of each character.
If each character occurs even number of
times, then it must be a palindrome.

How about character which occurs odd number of times?

Just check there is no more than one character that
appear an odd number of times in the string. Because
if there is one, then it must be in the middle of the palindrome.
So we can't have two of them.

"""

# Method 1: Using hashtable

def canPermutePalindrome(self, s):
    return sum(v % 2 for v in collections.Counter(s).values()) < 2

