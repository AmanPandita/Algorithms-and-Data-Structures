from p3 import heapSort
from p3 import MinPriorityQueue
# Driver code
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])


pq = MinPriorityQueue()
pq.insert(5)
pq.insert(2)
pq.insert(8)

print(pq.first())  # Output: 2
print(pq.remove_first())  # Output: 2
print(pq.first())  # Output: 5

