n = int(input())
while True:
    print(int(n), end=" ")
    if n == 1:
        break
    if n % 2 == 0:
        n /= 2
    else:
        n = 3*n + 1
    
    