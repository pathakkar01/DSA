#memorization
# dict , key will be arg to fo, value will the return value
# 2n  call in memo implementation o(N) time and o(n) space



def fib(n, memo = {}):
    if n in memo: return memo[n]
    if n<=2 :
        return 1
    memo[n] = fib(n-1, memo)+fib(n-2, memo)
    return memo[n]

print(fib(6))
print(fib(10))
print(fib(50))