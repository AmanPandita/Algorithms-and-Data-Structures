

import time
import random
from sorting import quicksort
from sorting import merge_sort
import numpy as np
import sys

sys.setrecursionlimit(10000000)
# from sorting import merge

import matplotlib.pyplot as plt

def generate_random_array(size):
    return [random.randint(0, size) for _ in range(size)]

def generate_sorted_random_array(size):
    random_array = [random.randint(0, size) for _ in range(size)]
    return sorted(random_array)


# sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
sizes = np.arange(100, 10000, 500)


times1 = []  # To store the time taken for each sorting
times2 = []

print("Results for Merge sort when randomly sorted")
for size in sizes:
    arr = generate_sorted_random_array(size)  # change this according to what's being returned above.
    start = time.time()
    merge_sort(arr, 0, len(arr)-1)
    # merge_sort(arr)
    end = time.time()
    
    time_taken = round((end - start), 7) * 1000
    times1.append(time_taken)  # Storing the time taken for sorting
    
    print(f"Size: {size}, Time taken: {time_taken} ms")



print("Results for Quick sort when randomly sorted")
for size in sizes:
    arr = generate_sorted_random_array(size)  # change this according to what's being returned above.
    start = time.time()
    quicksort(arr)
    end = time.time()
    
    time_taken = round((end - start), 7) * 1000
    times2.append(time_taken)  # Storing the time taken for sorting
    
    print(f"Size: {size}, Time taken: {time_taken} ms")

print(len(sizes), len(times1))


# print("Results for Merge sort when already sorted")
# for size in sizes:
#     arr = generate_sorted_random_array(size)  # change this according to what's being returned above.
#     start = time.time()
#     merge_sort(arr, 0, len(arr)-1)
#     end = time.time()
    
#     time_taken = round((end - start), 7) * 1000
#     times1.append(time_taken)  # Storing the time taken for sorting
    
#     print(f"Size: {size}, Time taken: {time_taken} ms")


# print("Results for Merge sort when already sorted")
# for size in sizes:
#     arr = generate_sorted_random_array(size)  # change this according to what's being returned above.
#     start = time.time()
#     quicksort(arr)
#     end = time.time()
    
#     time_taken = round((end - start), 7) * 1000
#     times2.append(time_taken)  # Storing the time taken for sorting
    
#     print(f"Size: {size}, Time taken: {time_taken} ms")

# print(len(sizes), len(times1))



# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, times1, '-r' ,marker='o', label='Merge Sort already sorted')
plt.plot(sizes, times2, '-g' ,marker='o', label='Quick Sort already sorted')
plt.xscale('log')
# plt.yscale('log')
plt.xlabel('Input Size')
plt.ylabel('Running Time (seconds)')
# plt.title('Running Times of Merge Sort and Quick Sort (Randomly Sorted Input)')
plt.title('Running Times of Merge Sort and Quick Sort (already Sorted Input)')
plt.legend()
plt.grid(True)
plt.show()