def solve(S, m, n):  
    t = [[0] * (n+1) for _ in range(m+1)]   
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                 t[0][j] = 0
            elif j == 0 :
                t[i][0] = 1
           
            elif S[i-1] <= n:
                t[i][j] = t[i-1][j] + t[i][j-S[i-1]]
            else:
                t[i][j] = t[i-1][j]
    print(t[m][n])


m = 3
n = 4

s = [1,2,3]
solve(s, m , n)

