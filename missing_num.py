n = int(input())
nums = list(map(int,input().strip().split()))
expectsum =  n * (n+1)/2
#print(expectsum, sum(nums))
print(int(expectsum - sum(nums)))