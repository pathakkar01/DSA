n = int(input())
A = list(map(int,input().strip().split()))
step = 0
for i in range(1,n):
    if A[i] > A[i-1]:
        continue
    elif A[i] < A[i-1]:
        step += (A[i-1] - A[i])
        A[i] += (A[i-1] - A[i])
print(step)