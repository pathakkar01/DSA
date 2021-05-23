def subSetSum(sum, arr, n):
    t = [[-1]*(sum+1) for i in range(n+1)]
    for i in range(sum+1):
        t[0][i] = False
    for i in range(n+1):
        t[i][0] = True
    for i in range(1,n+1):
        for j in range(1,sum+1):
            t[i][j] = t[i-1][j]
            if j >= arr[i-1]:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]

    
    return t[n]

def MinSubsetSum(arr,n):
    ran = sum(arr)
    t = subSetSum(ran, arr, n)
    print(ran)
    v = []
    m = float('inf')
    print(t)
    for i in range(1,(ran//2 +1)):
        print(i)
        if t[i] == True:
            v.append(i)
    print(v)
    for i in range(len(v)):
        m = min(m, ran - 2*v[i])
    return m
arr = [1,6,11,5]
print(MinSubsetSum(arr, 4))

        