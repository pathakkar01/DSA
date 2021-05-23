
arr = [1]
sum = 2
"""
def subSetSum(sum, arr, n):
    t = [[-1]*(sum+1) for _ in range(n+1)]
    if sum ==0:
        return 1
    if n == 0:
        return 0
    if t[n][sum] != -1:
        return t[n][sum]
    if arr[n-1] <= sum:
        t[n][sum] = subSetSum(sum-arr[n-1], arr, n-1) + subSetSum(sum, arr, n-1)
        return t[n][sum]
    else:
        t[n][sum] = subSetSum(sum, arr, n-1)
        return t[n][sum]

print(subSetSum(sum, arr, len(arr)))
"""

def subSetSum(s, nums, n):
    #n = len(nums)
    t = [[-1]*(s+1) for _ in range(n+1)]
    for i in range(s+1):
        t[0][i] = 0
    for i in range(n+1):
        t[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,s+1):
            t[i][j] = t[i-1][j]
            if j >= nums[i-1]:
                t[i][j] = t[i-1][j] + t[i-1][j-nums[i-1]]
    print(t)
    return t[n][s]
print(subSetSum(sum, arr, len(arr)))

