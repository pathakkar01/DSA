
"""def solve(ls, n, N):
    if n==0:
        return 0
    if N == 0:
        return 0
    if t[n] != -1:
        return t[n]
    if ls[N-1] <= n:
        t[n] = max(1+solve(ls, n-ls[N-1], N), solve(ls, n, N-1))
        print(max(1+solve(ls, n-ls[N-1], N), solve(ls, n, N-1)))
        print(t)
        return t[n]
        
    else:
        t[n] = solve(ls,n, N-1)
        return t[n]"""

def solve(ls, n, N, t):
    for i in range(N):
        for j in range(n):
            if i ==0 or j ==0:
                t[i][j] =  0
            if ls[i-1] <= n:
                t[i][j] = max(1+t[i][j-ls[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    print(t)
    return t[N][n]



ls = [2,1,1]
n = 4
t = [[-1]*(n+1) for _ in range(4)]
print(t)
print(t)

print(solve(ls,4 ,3,t))