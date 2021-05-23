"""import math
t = int(input())

for _ in range(t):
    n, k, d = map(int, input().strip().split())
    A = list(map(int,input().strip().split()))
    if math.floor(sum(A)/k) > d :
        print(d)
    else:
        print(math.floor(sum(A)/k))
    ############################# Second problem ####################33
t = int(input())
for _ in range(t):
    n = int(input())
    str1 = input()
    ans = ""
    for i in range(0,n-1,4):
        s = str1[i:i+4]
        if s[0] == '0':
            if s[1] == '0':
                if s[2] == '0':
                    if s[3] == '0':
                        ans += "a"
                    else:
                        ans += "b"
                else:
                    if s[3] == '0':
                        ans += "c"
                    else:
                        ans += "d"
            else:
                if s[2] == '0':
                    if s[3] == '0':
                        ans += "e"
                    else:
                        ans += "f"
                else:
                    if s[3] == '0':
                        ans += "g"
                    else:
                        ans += "h"
        else:
            if s[1] == '0':
                if s[2] == '0':
                    if s[3] == '0':
                        ans += "i"
                    else:
                        ans += "j"
                else:
                    if s[3] == '0':
                        ans += "k"
                    else:
                        ans += "l"
            else:
                if s[2] == '0':
                    if s[3] == '0':
                        ans += "m"
                    else:
                        ans += "n"
                else:
                    if s[3] == '0':
                        ans += "o"
                    else:
                        ans += "p"
print(ans)

########################### Third ########################## 

t = int(input())

for _ in range(t):
    n, m = map(int,input().strip().split())
    a = list(map(int, input().strip().split()))[:n]
    b = list(map(int, input().strip().split()))[:m]
    count = 0
    if sum(a) > sum(b):
        print(0)
    else:
        a.sort()
        b.sort(reverse=True)
        i =0
        while(sum(a) <= sum(b)):
            if i >= len(a) or i >= len(b):
                i = -1
                break
            a[i], b[i] = b[i], a[i]
            i += 1
        print(i)
    

######################## Fourth #####################

t = int(input())

for _ in range(t):
    n, k, x, y= map(int,input().strip().split())

    k = (k-1) % 4
    if x == y:
        print(n, n)
    else:
        ans = []
        if x > y :
            ans = [[n,n+y-x],[n+y-x, n],[0,x-y], [x-y, 0]]
        else:
            ans = [[x+n-y,n], [n, x+n-y], [y-x, 0], [0, y-x]]
    ans = ans[k]
    print(ans[0],ans[1])"""

import queue

def isSubSequence(string1, string2, m, n):
    # Base Cases
    if m == 0:
        return True
    if n == 0:
        return False
 
    
    if string1[m-1] == string2[n-1]:
        return isSubSequence(string1, string2, m-1, n-1)
 

    return isSubSequence(string1, string2, m, n-1)

def genBinaryNo(s):
    if not(isSubSequence("0", s, 1, len(s))):
        return("0")
    else:
        q =queue.Queue()

        q.put("1")

        while True:
            s1 = q.get()
            if not(isSubSequence(s1, s, len(s1), len(s))):
                return s1
            s2 = s1
            q.put(s1 + "0")
            q.put(s2 + "1")

T = int(input())
for _ in range(T):
    s = input()
    print(genBinaryNo(s))



