#https://www.codechef.com/LTIME91B/problems/HRSCPMTR

t = int(input())
for _ in range(t):
    n, m  = map(int, input().strip().split())
    arr = []
    count = 0
    for i in range(n):
        l=list(map(int,input().split()))
        arr.append(l)
    
    
    for i in range(1,n):
        for j in range(1,m):
            if arr[i][j] != arr[i-1][j-1]:
                count +=1
    q = int(input())
    while(q):
        x, y, v = map(int, input().strip().split())
        x -= 1
        y -= 1
        old = arr[x][y]
        arr[x][y] = v
        if x-1 >= 0 and y-1 >= 0:
            if arr[x][y] == arr[x-1][y-1] and old != arr[x][y]:
                count -=1
        if x+1 < n and y+1 < m:
            if arr[x][y] == arr[x+1][y+1] and old != arr[x][y]:
                count -=1
        if x-1 >= 0 and y-1 >= 0:
            if arr[x][y] != arr[x-1][y-1] and old == arr[x-1][y-1]:
                count +=1
        if x+1 < n and y+1 < n:
            if arr[x][y] != arr[x+1][y+1] and old == arr[x+1][y+1]:
                count +=1
        print("YES" if count == 0 else "NO")
        q -= 1
