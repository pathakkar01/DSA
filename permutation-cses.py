n = int(input())
if n == 1:
    print("1")
elif n == 4:
    print("2 4 1 3")
elif(n <= 3):
    print("NO SOLUTION")
else:
    for i in range(n, 0, -2):
        print(i, end=" ")
    for i in range(n-1, 0, -2):
        print(i, end=" ")
