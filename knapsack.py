"""t = [[-1]*1002 for _ in range(1002)]
val = [60, 100, 120 ]
wt = [10, 20, 30 ]
W = 50
n = len(val)



        ##### Recursive + Memorization = Bottum-Up approch #######
def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
            return 0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1]+knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))
        return t[n][W]
    elif wt[n-1] > W :
        t[n][W] = knapSack(W, wt, val, n-1)
        return t[n][W]
print(knapSack(W, wt, val, n))


###### Top-Down approch ########

def knapSack(W, wt, val, n):
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wt[i-1] <= j :
                t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][W]

print(knapSack(W, wt, val, n))"""

ans = ""
for i in ["o", "l"]:
    ans += i
print(ans)