def partition(arr, pivot, low, high):
    # 0 to j-1 - <= pivot
    # j to i-1 - > pivot
    # i to end - unknown
    i, j = low, low
    while i <= high :
        if arr[i] > pivot:
            i +=1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    return j-1

def quickSort(arr, low, high):
    if low >= high:
        return
    pivot = arr[high]

    pi = partition(arr, pivot, low,  high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)
arr = [23,10,99, 897, 34, 0]    
quickSort(arr,0, 5)
print(arr)
