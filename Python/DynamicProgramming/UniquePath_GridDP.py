#!/usr/bin/python

# Method 1: Using Maths and no DP

"""
This is a combinatorial problem and can be solved without DP. For mxn grid,
robot has to move exactly m-1 steps down and n-1 steps right and these can be done in any order.
For the eg., given in question, 3x7 matrix, robot needs to take 2+6 = 8 steps with 2 down and 6
right in any order. That is nothing but a permutation problem. Denote down as 'D' and right as 'R',
following is one of the path :-
D R R R D R R R
We have to tell the total number of permutations of the above given word. So, decrease both m & n
by 1 and apply following formula:-

Total permutations = (m+n)! / (m! * n!)
"""

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)


# Method 2: DP in O(m*n)


    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        dp = [[1 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# Method 3: DP in O(n)

    def uniquePaths(self, m, n):
        """

        :param self:
        :param m:
        :param n:
        :return:
        """
        if not m or not n:
            return 0
        cur = [1] * n
        for i in xrange(1, m):
            for j in xrange(1, n):
                cur[j] += cur[j-1]
        return cur[-1]