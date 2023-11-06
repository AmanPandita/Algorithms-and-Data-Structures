# adapted from GeekForGeeks



def siftDown(arr, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child >= end:
            break

        if child + 1 < end and arr[child] < arr[child + 1]:
            child += 1

        if arr[root] >= arr[child]:
            break

        arr[root], arr[child] = arr[child], arr[root]
        root = child

def heapSort(arr):
    n = len(arr)

    # Build a max-heap from bottom to top
    for i in range(n // 2, -1, -1):
        siftDown(arr, i, n)

    # Extract elements one by one and maintain heap property
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # In-place swap
        siftDown(arr, 0, i)

# Driver code
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])




class MinPriorityQueue:
    def __init__(self):
        self.heap = []
    
    def insert(self, priority):
        self.heap.append(priority)
        self._upheap()
    
    def first(self):
        return self.heap[0] if self.heap else None
    
    def remove_first(self):
        if not self.heap:
            return None
        min_priority = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._downheap()
        return min_priority
    
    def _upheap(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break
    
    def _downheap(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_child_index = index
            
            if (left_child_index < len(self.heap) and 
                self.heap[left_child_index] < self.heap[smallest_child_index]):
                smallest_child_index = left_child_index
                
            if (right_child_index < len(self.heap) and 
                self.heap[right_child_index] < self.heap[smallest_child_index]):
                smallest_child_index = right_child_index
                
            if smallest_child_index == index:
                break
                
            self.heap[index], self.heap[smallest_child_index] = \
                self.heap[smallest_child_index], self.heap[index]
            index = smallest_child_index

pq = MinPriorityQueue()
pq.insert(5)
pq.insert(2)
pq.insert(8)

print(pq.first())
print(pq.remove_first())
print(pq.first())

print(pq.first())
print(pq.remove_first())
print(pq.first())
