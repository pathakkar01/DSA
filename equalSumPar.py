""""def subSetSum(s, nums, n):
    t = [[-1]*(s+2) for _ in range(n+2)]
    if t[n][s] != -1:
        return t[n][s]
    if s==0:
        return True
    if n == 0:
        return False
    if nums[n-1] <= s:
        t[n][s] = subSetSum(s-nums[n-1], nums, n-1) or subSetSum(s, nums, n-1)
        return t[n][s]
    else:
        t[n][s] = subSetSum(s, nums, n-1)
        return t[n][s]
def canPartition(nums):
    if sum(nums)% 2 != 0:
        return False
    else:
        return subSetSum(int(sum(nums)/2), nums, len(nums))"""
def canPartition(nums):
    if sum(nums) % 2 != 0:
        return False
    s = sum(nums) // 2
    n = len(nums)
    t = [[-1]*(s+1) for _ in range(n+1)]
    for i in range(s+1):
        t[0][i] = False
    for i in range(n+1):
        t[i][0] = True
    for i in range(1,n+1):
        for j in range(1,s+1):
            t[i][j] = t[i-1][j]
            if j >= nums[i-1]:
                t[i][j] = t[i-1][j] or t[i-1][j-nums[i-1]]
    return t[n][s]

print(canPartition([3, 1, 1, 2, 2]))