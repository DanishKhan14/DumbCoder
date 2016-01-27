#!/usr/bin/python

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        #we can reuse the matrix to save space if the requirement does not mention
        # not to modify the original matrix
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        #need to take care special case
        if obstacleGrid[0][0]: return 0

        obstacleGrid[0][0] = 1

        #update the first column
        for i in range(1, m):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] else obstacleGrid[i-1][0]
        #update the first row
        for j in range(1, n):
            obstacleGrid[0][j] = 0 if obstacleGrid[0][j] else obstacleGrid[0][j-1]
        #update the rest part
        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] else obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]