#N digit binary no  where n0 of 1's is greter than no of 0's in its all prefix

def solve(op, ones, zeros, N, ans):
    if N == 0:
        ans.append(op)
        return
    
    op1 = op + "1"
    
    solve(op1, ones+1, zeros, N-1, ans)
    if ones > zeros:
        op2 = op + "0"
        solve(op2, ones, zeros+1, N-1, ans)
    

N = 3
ones = 0
zeros = 0
op = ""
ans = []
solve(op, ones, zeros, N, ans)
print(ans)

