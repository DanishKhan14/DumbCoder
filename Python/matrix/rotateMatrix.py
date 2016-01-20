#!/usr/bin/python

"""
Given mxn matrix. rotate by 90 degrees

Solution:
First row becomes last column. Second row becomes second last col, likewise

dstMatrix[col][m - row - 1] = srcMatrix[row][col]

"""

def rotate(self, board):

    n = len(board)
    dst = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            dst[j][n - i - 1] = board[i][j]

    for i in range(n):
        for j in range(n):
            board[i][j] = dst[i][j]


## In Place Solution

"""
First transpose then reverse

Example:
1 2 3 --> 1 4 7 --> 7 4 1
4 5 6 --> 2 5 8 --> 8 5 2
7 8 9 --> 3 6 9 --> 9 6 3

"""

def inPlaceRotate(self, board):

    n = len(board)

    #Transpose
    for i in range(n):
        for j in range(i+1, n):
            temp = board[i][j]
            board[i][j] = board[j][i]
            board[j][i] = temp

    #Reverse
    for i in range(n):
        for j in range(n//2):
            temp = board[i][j]
            board[i][j] = board[i][n-j-1]
            board[i][n-j-1] = temp



