def reverse(arr, rev): 
    if len(arr) == 0: 
        return
    curr = arr[1:]
    reverse(curr,rev)
    rev.append(curr)
    return rev
    
rev = reverse([1,2,3],[])
print(rev)