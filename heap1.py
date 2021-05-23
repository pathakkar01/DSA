import heapq_max

arr = [23, 5, 7, 8, 12, 100, 45]
k = 5
heap = []

for i in range(len(arr)):
    heapq_max.heappush_max(heap, arr[i])
    
    if len(heap) > k:
        heapq_max.heappop_max(heap)
    print(heap)

print(heap[0])
