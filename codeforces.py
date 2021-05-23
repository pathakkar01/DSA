"""tc = int(input())
 
for _ in range(tc):
    
    n = int(input())
    A = list(map(int,input().strip().split()))
    for i in set(A):
        if A.count(i) >= 2:
                A.remove(i)
                A.append(i+1)
    print(len(set(A)))
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

def rev(ls,length):
    if length == 1:
        print(ls[0])
        return
    print(length,ls[length-1])
    rev(ls,length-1)
print(rev("pooj", 4))

def sort1(ls):
    if n == 1:
        return 
    temp = ls[len(ls)-1]
    ls.pop()
    sort(ls)
    insert(ls,temp)



n = int(input())
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(100))

def insert(ls, temp):
    if len(ls) == 0 or ls[len(ls)-1] <= temp:
        ls.append(temp)
        return
    val = ls[len(ls)-1]
    ls.pop()
    sort(ls)
    insert(ls, temp)
    ls.append(val)
    print(ls)


def sort(ls):
    if len(ls) == 1:
        return
    print(len(ls))
    temp = ls[len(ls) -1]
    ls.pop()
    insert(ls, temp)
    print(ls)

ls = list(map(int, input().strip().split()))
sort(ls)
print(ls)

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)"""


print("pooja" > "ponam")
