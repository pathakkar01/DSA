def mergeArr(a, b):
    i, j, k =0, 0, 0
    ans = [0 for i in range(len(a)+len(b))]
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            ans[k] = a[i]
            k +=1 
            i += 1
        else:
            ans[k] = b[j]
            k += 1
            j += 1
    while i < len(a):
        ans[k] = a[i]
        i += 1
        k += 1
    while j <len(b):
        ans[k] = b[j]
        j += 1
        k += 1
    #print(ans)
    return ans
def mergeSort(arr, low, high):
    if low == high:
        
        return [arr[low]]

    mid = (low + high) // 2
    

    fh = mergeSort(arr, low, mid) 
    
    sh = mergeSort(arr, mid+1, high)
    ans = mergeArr(fh, sh)
    #print(ans)
    return ans

print(mergeSort([67, 2, 99, 12, 23,89, 100,56], 0, 7))
