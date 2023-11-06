###########################   Adapted from Geek For Geek   ###########################



#  Max-Heap ----------------------------------------------------------------------------------------------------


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # Check if left child of root exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Check if right child of root exists and is greater than the largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)  # call max heapify on the reduced heap






#  MinPriority Queue----------------------------------------------------------------------------------------------------





class MinPriorityQueue:
    def __init__(self):
        self.heap = []
    
    def insert(self, priority):
        # Inserting the priority at the end of the heap
        self.heap.append(priority)
        
        # Up-heaping: Fixing the heap property from bottom to top
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break
    
    def first(self):
        if self.heap:
            return self.heap[0]  # Returning the minimum priority
        else:
            return None
    
    def remove_first(self):
        if not self.heap:
            return None
        
        # Extracting the minimum priority
        min_priority = self.heap[0]
        
        # Moving the last priority to the root
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Down-heaping: Fixing the heap property from top to bottom
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            
            # Finding the smallest child
            smallest_child_index = None
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[index]:
                smallest_child_index = left_child_index
            
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[index] and \
               (smallest_child_index is None or self.heap[right_child_index] < self.heap[left_child_index]):
                smallest_child_index = right_child_index
            
            # If the heap property is not violated, break
            if smallest_child_index is None:
                break
            
            # Swapping the current node with the smallest child
            self.heap[index], self.heap[smallest_child_index] = \
                self.heap[smallest_child_index], self.heap[index]
            
            index = smallest_child_index
        
        return min_priority