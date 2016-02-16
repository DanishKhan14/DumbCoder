#!/usr/bin/python

    def lcs(x, y):
        n = len(x)
        m = len(y)
        table = dict()  # a hashtable, but we'll use it as a 2D array here

        for i in range(n+1):     # i=0,1,...,n
            for j in range(m+1):  # j=0,1,...,m
                if i == 0 or j == 0:
                    table[i, j] = 0
                elif x[i-1] == y[j-1]:
                    table[i, j] = table[i-1, j-1] + 1
                else:
                    table[i, j] = max(table[i-1, j], table[i, j-1])
        return table[m,n]
    # Reconstruct

    def recon(i, j):
        if i == 0 or j == 0:
            return []
        elif x[i-1] == y[j-1]:
            return recon(i-1, j-1) + [x[i-1]]
        elif table[i-1, j] > table[i, j-1]: #index out of bounds bug here: what if the first elements in the sequences aren't equal
            return recon(i-1, j)
        else:
            return recon(i, j-1)

    return recon(n, m)


# Method

def LCS(X, Y):
    m, n = len(X), len(Y)
    C = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C[-1][-1]