#!/usr/bin/python

   # O(m*n)
    def minPathSum(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
        dp[0][0] = grid[0][0]
        for i in xrange(1, r):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in xrange(1, c):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

    # O(2*n) space
    def minPathSum2(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        pre = cur = [0] * c
        pre[0] = grid[0][0]
        for i in xrange(1, c):
            pre[i] = pre[i-1] + grid[0][i]
        for i in xrange(1, r):
            cur[0] = pre[0] + grid[i][0]
            for j in xrange(1, c):
                cur[j] = min(cur[j-1], pre[j]) + grid[i][j]
            pre = cur
        return cur[-1]

    # O(n) space
    def minPathSum(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        cur = [0] * c
        cur[0] = grid[0][0]
        for i in xrange(1, c):
            cur[i] = cur[i-1] + grid[0][i]
        for i in xrange(1, r):
            cur[0] += grid[i][0]
            for j in xrange(1, c):
                cur[j] = min(cur[j-1], cur[j]) + grid[i][j]
        return cur[-1]

    # change the grid itself
    def minPathSum4(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        for i in xrange(1, c):
            grid[0][i] += grid[0][i-1]
        for i in xrange(1, r):
            grid[i][0] += grid[i-1][0]
        for i in xrange(1, r):
            for j in xrange(1, c):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]