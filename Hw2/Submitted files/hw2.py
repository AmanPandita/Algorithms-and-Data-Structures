import time
import random
import matplotlib.pyplot as plt
import numpy as np
import sys


# quicksort function

def quicksort(arr):
    if len(arr) <= 1:
        return arr
 
    pivot = random.choice(arr)
    # pivot = arr[0]

    left_arr, mid_arr, right_arr = [], [], []
    for num in arr:
        if num < pivot:
            left_arr.append(num)
        elif num == pivot:
            mid_arr.append(num)
        else:
            right_arr.append(num)
    return quicksort(left_arr) + mid_arr + quicksort(right_arr)



#-----------------------------------------------


# mergesort function


def merge_sort(arr, l, r):

    if l < r:

        mid = l + (r - l) // 2

        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        
        merge(arr,l,mid,r)


### function to merge divided arrary
def merge(arr, l, mid, r):

    n1 = mid - l + 1         # l......m-1
    n2 = r - mid            # mid.....r



    
    # lets create temp array and defining size


    left_arr = [0] * n1
    right_arr = [0] * n2

    #dividing orignal arr to add data in left and right array


    for i in range(0, n1):
        left_arr[i] = arr[l + i]

    for j in range(0,n2):
        right_arr[j] = arr[mid + j + 1]

    # Merging both arrays back in one


    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k +=1

    # if any elements are remaining 
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

