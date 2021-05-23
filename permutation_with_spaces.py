"""def solve(ip, op, ans):
    if len(ip) == 0:
        ans.append(op)
        return
    op1 = op + ip[0]
    op2 = op + " " + ip[0]
    ip =ip[1:]
    solve(ip, op1, ans)
    solve(ip, op2, ans)
s = input()
op = s[0]
ip = s[1:]
ans = []
solve(ip, op, ans)
print(ans)

T = int(input())
for _ in range(T):
    N, k = map(int, input().strip().split())
    s = input()
    score = 0
    for i in range(0, int(N/2)):
        print(i, N-i)
        if s[i] != s[N-i-1]:
            score  += 1
    print(score)
    if score < k:
        print(k - score)
    else:
        print(0)"""
