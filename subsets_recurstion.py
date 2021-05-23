def solve(ip, op, ls):
    if len(ip) == 0:
        ls.append(op)
        return 
    op1 = op
    op2 = op + ip[0]
    ip = ip[1:]
    solve(ip, op1, ls)
    solve(ip, op2, ls)


ip= input()
ls = []
solve(ip,"", ls)
print(ls)
