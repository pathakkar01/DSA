""""try:
    t = int(input())
    while(t):
        n, k = map(int, input().strip().split())
        #print(n,k)
        A = list(map(int,input().strip().split()))
        print(sum(A))
        if sum(A) % k == 0:
            
            print(0)
        else:
            print(1)
        t = t-1
except EOFError as e:
    print(end="")
tc = int(input())
 
for _ in range(tc):
    
    n = int(input())
    s = input()
    p = input()
    
    zeros = ones = 0
    
    for i in range(n):
        if s[i] != p[i]:
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
    
    if zeros != ones:
        print("No")
        continue
    
    c1 = 0
    ans = True
    
    for i in range(n):
        if s[i] != p[i]:
            if s[i] == '0':
                if c1 > 0:
                    c1 -= 1
                else:
                    ans = False
                    break
            else:
                c1 += 1
                
    print("Yes" if ans else "No")

T = int(input())
for i in range(T):
    N, k = map(int, input().strip().split())
    s = input()
    score = 0
    for i in range(0, int(N/2)):
        #print(i, N-i)
        if s[i] != s[N-i-1]:
            score  += 1
    
    print("Case #" + str(i) + ": " + str(abs(score-k)))


try:
    T = int(input())
    for _ in range(T):
        n, m , k = map(int, input().strip().split())
        mat, count = [], 0
        for _ in range(n):
            mat.append(list(map(int, input().strip().split())))
        maxsize = max(n, m)
        mat2 = []
        for i in range(n):
            sum1 = 0
            ls = []
            for j in range(m):
                sum1 += mat[i][j]
                ls.append(sum1)
            mat2.append(ls)
        print(mat2)
        for i in range(m):
            sum1 = 0
            for j in range(n):
                sum1 += mat2[j][i]
                mat2[j][i] = sum1
        print(mat2)
        for q in range(1, maxsize):
            for i in range(n-q+1):
                print(i)
                for j in range(m-q+1):
                    print("j",j, q)
                    s = mat2[i+q-1][j+q-1]
                    for p in range(i, i+q):
                        for r in range(j, j+q):
                            print(mat[p][r])
                            s += mat[p][r]
                    print(s)
                    if s >= k *q * q:
                        #print(q,i,j)
                        #print(n-i, count)
                        
                        print("count",m - j -q+1)
                        count += m - j -q+1
                        break
                        
    print(count)
except EOFError as e:
    print(end="") """

def asteroidCollision(nums):
        print("somethim]ng")
        stack = [nums[0]]
        for i in range(1,len(nums)):
            if stack[-1] < 0:
                stack.append(nums[i])
            elif stack[-1] > 0:
                if nums[i] > 0:
                    stack.append(nums[i])
                else:
                    while True:
                        print(stack)
                        if abs(nums[i]) > stack[-1]:
                            stack.pop()
                            if len(stack) == 0:
                                stack.append(nums[i])
                                break
                        elif abs(nums[i]) < stack[-1]:
                            continue
                        else:
                            stack.pop()
        return stack
print("here")
print(asteroidCollision([10, 2, -1]))

