#!/usr/bin/python

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0,9):
            row = []
            col = []
            square = []
            for j in range(0,9):
                row.append(False)
                col.append(False)
                square.append(False)
            for j  in range(0,9):
                if board[i][j] != '.':
                    if board[i][j].isdigit() and int(board[i][j])>0 and int(board[i][j])<=9 and not row[int(board[i][j])-1]:
                        row[int(board[i][j])-1] = True
                    else:
                        return False
                if board[j][i] != '.':
                    if board[j][i].isdigit() and int(board[j][i])>0 and int(board[j][i])<=9 and not col[int(board[j][i])-1]:
                        col[int(board[j][i])-1] = True
                    else:
                        return False
                rowSquare = int(i / 3)*3 + int(j / 3);
                colSquare = (i % 3)*3 + j % 3;
                if board[rowSquare][colSquare] != '.':
                    if board[rowSquare][colSquare].isdigit() and int(board[rowSquare][colSquare])>0 and int(board[rowSquare][colSquare])<=9 and not square[int(board[rowSquare][colSquare])-1]:
                        square[int(board[rowSquare][colSquare])-1] = True
                    else:
                        return False
        return True