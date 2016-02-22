"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation
"""

# [TLE]  Method 1: Brute Force. Keep adding one char at a time in rev order
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        new = s
        for i in range(l):
            new = s[l-i:l][::-1]  + s
            if self.isPalindrome(new):
                return new
        return new

    def isPalindrome(self, a):
        return a == a[::-1]