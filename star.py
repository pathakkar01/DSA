#[print("@ ") for i in reversed(range(6-j-1)) for j in range(6)]

for i in range(6):
    for j in range(6-i-1):
        print(" ", end="")
    for j in reversed(range(6-i-1,6,1)):
        print("@ ", end="")
    print("\n")
