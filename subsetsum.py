t = [[-1]*101 for _ in range(1001)]
arr = [1, 5, 3, 7, 4]
sum = 20
"""
def subSetSum(sum, arr, n):
    if sum ==0:
        return True
    if n == 0:
        return False
    if t[n][sum] != -1:
        return t[n][sum]
    if arr[n-1] <= sum:
        t[n][sum] = subSetSum(sum-arr[n-1], arr, n-1) or subSetSum(sum, arr, n-1)
        return t[n][sum]
    else:
        t[n][sum] = subSetSum(sum, arr, n-1)
        return t[n][sum]

print(subSetSum(sum, arr, len(arr)))"""

def subSetSum(sum, arr, n):
    for i in range(sum+1):
        t[0][i] = False
    for j in range(n+1):
        t[i][0] = True
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]
    return t[n][sum]
print(subSetSum(sum, arr, len(arr)))

