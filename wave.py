"""nums = [1,3,4,2,2]
nums.sort()
print(nums)
low, high = 0, len(nums)
while high != low:
    mid = int((high+low)/2)
    print(high, low, mid)
    if nums[mid] != mid + 1:
        high = mid
    else:
        low = mid
print(high)"""


"""t = int(input())
for i in range(t) :
    n, b = int(input().split(" "))
    A = list(map(int, input().strip().split()))
    A.sort()
    budget=0
    count = 0
    for i in range(len(A)):
        if budget + A[i] < b:
            budget = budget + A[i] 
            count += 1
        else:
            break
    print(Case #1: ,count)

def gfg(x,l=[]): 
    for i in range(x): 
        l.append(i*i) 
    print(l)  
  
gfg(2) 
gfg(3,[3,2,1]) 
gfg(3) 

dictionary = {'GFG' : 'geeksforgeeks.org', 
              'google' : 'google.com', 
              'facebook' : 'facebook.com'
              } 
del dictionary['google']; 
for key, values in dictionary.items(): 
    print("output",key) 
dictionary.clear(); 
for key, values in dictionary.items(): 
    print(key) 
del dictionary; 
for key, values in dictionary.items(): 
    print(key) 

if 0:
    print(“hai/”)

else:
    print(“0 is falsy!”)"""

from string import punctuation

str1 = '/*Sam is @student & painter!!'
for char in str1:
    str1 = str1.replace(char, "$")
print(str1)