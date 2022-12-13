from array import array
import random
from time import perf_counter
from typing import List
from math import *


def Merge(beg, end, mid, array):
    n1 = mid - beg + 1  # left sub array size
    n2 = end - mid  # right sub array size
    LeftArray = [None] * n1
    RightArray = [None] * n2

    i = 0
    while i < n1:
        LeftArray[i] = array[beg + i]

        i = i + 1
    j = 0
    while j < n2:
        RightArray[j] = array[mid + 1 + j]
        j += 1

    i, j, k = 0, 0, beg

    while i < n1 and j < n2:
        if LeftArray[i] <= RightArray[j]:
            array[k] = LeftArray[i]
            i += 1
        else:
            array[k] = RightArray[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = LeftArray[i]
        i = i + 1
        k += 1

    while j < n2:
        array[k] = RightArray[j]
        j += 1
        k += 1


def MergeSort(array: List, beg, end):
    mid = int((beg + end) // 2)
    if beg < end:
        MergeSort(array, beg, mid)
        MergeSort(array, mid + 1, end)
        Merge(beg, end, mid, array)
    else:
        return


def is_sorted(array: List):
    flag = 0
    for i in range(0, len(array) - 1):
        if array[i] <= array[i + 1]:
            flag = 0
            continue
        else:
            flag = 1
            break

    if flag == 1:
        return "Not Sorted"

    else:
        return "Sorted"


# data = [random.randint(0, 100) for _ in range(8)]

# for _ in range(100):
exec_time = 0
size = random.randint(5000, 100000)
data = [random.randint(0, 100) for _ in range(size)]
start = perf_counter()
MergeSort(data, 0, size - 1)  # With Optimization
end = perf_counter()
exec_time = end - start
# comp = size * log10(size)
comp = size * log(size)
print(
    f"Data: {is_sorted(data)} |  Execution Time of Merge Sort Only: {exec_time:5f} | Data Size: {size} | Time Complexity O(nLogn): {comp} | Difference O() - exec_time): {comp - exec_time}"
)

# data = [10, 8, 65, 3, 34, 25, 83, 20]
