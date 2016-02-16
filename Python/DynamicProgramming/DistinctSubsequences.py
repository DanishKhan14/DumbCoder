"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.


"""

    def numDistinct(self, S, T):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Method 1: DP O(mn) time O(mn) space

        num = [[0 for x in range(len(T)+1)] for x in range(len(S)+1)]
        for i in range(0, len(S)+1):
            num[i][0] = 1
        for i in range(1, len(T)+1):
            num[0][i] = 0
        for i in range(1, len(S)+1):
            for j in range(1, len(T)+1):
                    if i < j:
                        num[i][j] = 0
                    else:
                        if S[i-1] == T[j-1]:
                            num[i][j] = num[i-1][j-1]+num[i-1][j]
                        else:
                            num[i][j] = num[i-1][j]
        return num[len(S)][len(T)]

        # Method 2: DP  O(n) space

        l1, l2 = len(s)+1, len(t)+1
        cur = [0] * l2
        cur[0] = 1
        for i in xrange(1, l1):
            pre = cur[:]
            for j in xrange(1, l2):
                cur[j] = pre[j] + pre[j-1]*(s[i-1] == t[j-1])
        return cur[-1]