def FindSecodLargestNumber(arr):
    """if len(arr) < 2:
        return "Error"
    second = -1
    largest = -1

    for i in range(len(arr)):
        if largest < arr[i] :
             largest = arr[i]

        if largest != arr[i] and largest > second:
            second, largest = largest, second
    if second == -1:
        return "The Second largest Element Does not Exist"
    else:
        return "The second largest element is:" + str(largest)

n = list(map(int,input().strip().split()))
print(FindSecodLargestNumber(n))"""
    arr = list(set(arr))
    if len(arr) < 2:
        return "The Second largest Element Does not Exist"
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]
        #print(arr)
    return "The second largest element is:" + str(arr[len(arr)-2])
n = list(map(int,input().strip().split()))
print(FindSecodLargestNumber(n))
