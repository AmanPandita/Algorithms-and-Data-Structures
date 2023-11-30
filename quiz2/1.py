# import random


# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
 
#     # pivot = random.choice(arr)
#     pivot = arr[len(arr)//2]
#     # print(pivot)
#     # pivot = arr[0]

#     left_arr, mid_arr, right_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             left_arr.append(num)
#         elif num == pivot:
#             mid_arr.append(num)
#         else:
#             right_arr.append(num)

        
#         print("The step did", arr)
#     return quicksort(left_arr) + mid_arr + quicksort(right_arr)


# arr = [2, 1, 5, 3, 4, 6]

# print(quick_sort(arr))







# def quick_sort(arr):
#     """ Quick sort function that sorts an array and returns a list of intermediate steps. """
#     intermediate_steps = []

#     def partition(low, high):
#         # Using the middle element as the pivot
#         pivot_index = (low + high) // 2
#         pivot = arr[pivot_index]

#         print(pivot)
#         arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
#         i = low - 1
#         for j in range(low, high):
#             if arr[j] < pivot:
#                 i += 1
#                 arr[i], arr[j] = arr[j], arr[i]
        
#         arr[i + 1], arr[high] = arr[high], arr[i + 1]
#         return i + 1

#     def quick_sort_recursive(low, high):
#         if low < high:
#             pi = partition(low, high)
#             intermediate_steps.append(arr[:])  # Copying current state of array
#             quick_sort_recursive(low, pi - 1)
#             quick_sort_recursive(pi + 1, high)

#     quick_sort_recursive(0, len(arr) - 1)
#     return intermediate_steps

# # The array to be sorted
# arr = [2, 1, 5, 3, 4, 6]

# # Performing Quick Sort
# quick_sort_steps = quick_sort(arr)
# quick_sort_steps




from graphviz import Digraph

def draw_heap(heap, filename):
    dot = Digraph(comment='Binary Heap')

    for i, value in enumerate(heap):
        dot.node(str(i), str(value))

        # Adding edges to parent if not root
        if i != 0:
            dot.edge(str((i - 1) // 2), str(i))

    dot.render(filename, format='png', cleanup=True)
    return filename + '.png'

# Initial heap
initial_heap = [4, 6, 5, 19, 11, 8]

# Heap after first deleteMin()
first_delete_heap = [5, 6, 8, 19, 11]  # 4 (min) is removed and heap is restructured

# Heap after second deleteMin()
second_delete_heap = [6, 11, 8, 19]  # 5 (new min) is removed and heap restructured again

# Drawing the heaps
initial_heap_path = draw_heap(initial_heap, '/mnt/data/initial_heap')
first_delete_heap_path = draw_heap(first_delete_heap, '/mnt/data/first_delete_heap')
second_delete_heap_path = draw_heap(second_delete_heap, '/mnt/data/second_delete_heap')

initial_heap_path, first_delete_heap_path, second_delete_heap_path

