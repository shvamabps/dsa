from time import perf_counter
from typing import List
import random
from math import *


def partition_low(high, low, array):
    i = low + 1
    j = high
    pivot = low

    while i < j:
        while array[pivot] >= array[i]:
            i = i + 1

        while array[pivot] < array[j]:
            j = j - 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    array[pivot], array[j] = array[j], array[pivot]

    return j


def QuickSort(high, low, array: List):
    if low >= high:  # termination condition for recurrsion
        return

    p = partition_low(high, low, array)

    QuickSort(p - 1, low, array)
    QuickSort(high, p + 1, array)


size = 50_000
data = [random.randint(0, 100) for _ in range(size)]

start = perf_counter()
QuickSort(size - 1, 0, data)  # Without Optimization
end = perf_counter()
print(f"Execution Time: {end - start:15f}")


# def is_sorted(array: List):
#     flag = 0
#     for i in range(0, len(array) - 1):
#         if array[i] <= array[i + 1]:
#             flag = 0
#             continue
#         else:
#             flag = 1
#             break

#     if flag == 1:
#         return "Not Sorted"

#     else:
#         return "Sorted"


# for _ in range(100):
#     exec_time = 0
#     size = random.randint(0, 1000)
#     data = [random.randint(0, 100) for _ in range(size)]
#     start = perf_counter()
#     QuickSort(size - 1, 0, data)  # With Optimization
#     end = perf_counter()
#     exec_time = end - start
#     # comp = size * log10(size)
#     comp = size * log(size)
#     print(
#         f"Data: {is_sorted(data)} |  Execution Time of Quick Sort Only: {exec_time:5f} | Data Size: {size} | Time Complexity O(nLogn): {comp} | Difference O() - exec_time): {comp - exec_time}"
#     )
