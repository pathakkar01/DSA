#https://www.codechef.com/LTIME91B/problems/THREE

t = int(input())

for _ in range(t):
    s = input()
    count = {}
    ans = 0
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    for i in count.values():
        ans += int(i/2)
    print(ans)