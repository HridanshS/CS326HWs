def PRINT-LCS(c, X, Y, i, j):
    if (i == 0 or j == 0):
        return
    if (X[i] == Y[j]):
        PRINT-LCS(c, X, Y, i-1, j-1)
        print(X[i])
    elif (c[i-1, j] > c[i, j-1]):
    #C is a 2D array w/ i rows and j cols
        PRINT-LCS(c, X, Y, i-1, j)
    else:
        PRINT-LCS(c, X, Y, i, j-1)