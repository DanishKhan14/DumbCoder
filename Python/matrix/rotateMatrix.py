#!/usr/bin/python

"""
Given mxn matrix. rotate by 90 degrees

Solution:
First row becomes last column. Second row becomes second last col, likewise

dstMatrix[col][m - row - 1] = srcMatrix[row][col]

"""

def rotate(self, board, m, n):

    dst = [[0 for j in range(m)] for i in range(n)]

    for i in range(m):
        for j in range(n):
            dst[j][m - i - 1] = board[i][j]

    return dst

