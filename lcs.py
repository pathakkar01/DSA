
def lcs(m, n, X, Y):
    t = [[-1]* (n+1) for _ in range(m+1)]
    if n==0 or m ==0 :
            return 0
    if t[m][n] != -1:
        return t[m][n]
    if X[m-1]  == Y[n-1]:
        t[m][n] =  1+lcs(m-1, n-1, X, Y)
        return t[m][n]
    else:
        t[m][n] = max(lcs(m-1, n, X, Y) , lcs(m, n-1, X, Y))
        return t[m][n]


def lcs1(m,n, text1, text2):
        t = [[0]* (n+1) for _ in range(m+1)]
        for i in range(m):
            t[i][0] = 0
        for i in range(n):
            t[0][i] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                
                if text1[i-1] == text2[j-1]:
                    
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        #print(t)
        printLCS(t, m, n, text1, text2)
        print(t)
        return t[m][n]

def printLCS(t, i, j, x, y):
    s = ""
    print(i, j)
    while( i> 0 and j > 0) :
        
        if x[i-1] == y[j-1]:
            print(x[i-1], y[j-1], i,j)
            s += x[i-1]
            i -=1
            j -= 1
        else:
            if t[i][j-1] > t[i-1][j]:
                j -= 1
            else :
                i -= 1
    print(s[::-1])
x = "cacbcbba"
y = "s"
print(lcs1(len(x), len(x), x, x[::-1]))
