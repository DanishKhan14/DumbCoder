"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


class Solution(object):
    def numDecodings(self, s):
        """

        A digit from index 1 have three condition

        '?10' or '?20' this can only divide into '10' or '20' , f(n) = f(n-2)

        '?26' this can divide into '6' or '26', f(n) = f(n-2)+f(n-1)

        '?09', '?27' this can only divide into '9' or '7' , f(n) = f(n-1)

        :type s: str
        :rtype: int
        """

        if not s or s.startswith('0'):
            return 0
        stack = [1, 1]
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '0' or s[i-1] > '2':  # only '10', '20' is valid
                    return 0
                stack.append(stack[-2])
            elif 9 < int(s[i-1:i+1]) < 27:         # '01 - 09' is not allowed
                stack.append(stack[-2]+stack[-1])
            else:                                  # other case '01, 09, 27'
                stack.append(stack[-1])
        return stack[-1]



        # Method 2:
                # if s begin with 0, return 0.
        if not len(s) or s[0] == '0':
            return 0

        total = 1
        pre = 1

        for i in range(1, len(s)):

            # when 0 appear, revert total to pre.
            if s[i] == '0':
                if not s[i-1] in '12':
                    return 0
                total = pre
                continue

            # if 2-digits num can be decoded, add pre to total,
            # and save the previous total to pre.
            elif int(s[i-1:i+1]) < 27 and s[i-1] != '0':
                pre, total = total, total+pre

            # all-is-well! forward to next step.
            else:
                pre = total

        return total