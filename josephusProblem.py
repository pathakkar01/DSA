def solve(n, k, ls, index):
    if len(ls) == 1:
        return
    index = (index+k) % len(ls)
    ls.pop(index)
    solve(n, k, ls, index)

k = int(input())
n = int(input())
k = k-1
index = 0
ls = [i+1 for i in range(n)]
solve(n, k, ls, 0)
print(ls[0])