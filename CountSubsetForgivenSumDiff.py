#Count the number of subset with a given difference
def CountSubsetSum(arr, n, s):
    t = [[-1]*(s+1) for _ in range(n+1)]
    for  i in range(0,s+1):
        t[0][i] = 0
    for i in range(0,n+1):
        t[i][0] = 1
    for i in range(1,n+1):
        for j in range(0, s+1):
            if j >= arr[i-1]:
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]
    print(t)
    return t[n][s]


def CountSubsetForGivenSumDiff(arr,n,diff):
    s1 = (diff + sum(arr)) // 2
    return CountSubsetSum(arr,n , s1)

print(CountSubsetForGivenSumDiff([0,0,0,0,0,0,0,0,1], 9, 1))