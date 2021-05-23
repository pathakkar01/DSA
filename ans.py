T = int(input())
for j in range(T):
    count =0 
    a = int(input())
    b = int(input())
    k = int(input())
    for i in range(a, b+1):
        if i % k == 0:
            count += 1
    print("Case " + str((j+1)) + ": " + str(count))