def insert(temp ,arr):
    if len(arr) ==0 or arr[-1] <= temp:
        arr.append(temp)
        return 
    val = arr[-1]
    arr.pop()
    insert(temp, arr)
    arr.append(val)
def sort(arr):
    if len(arr) == 1:
        return
    temp = arr[-1]
    arr.pop()
    sort(arr)
    insert(temp, arr)

arr = [100, 34, 67, 23, 12, 3, 9, 54,87]
sort(arr)
print(arr)
    
