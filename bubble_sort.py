import random
import time
from typing import List


def BubbleSort(arr: List):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def BubbleSortOptimized(arr: List):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


data = [random.randint(0, 100) for _ in range(50_000)]

# start = time.perf_counter()
# BubbleSort(data)  # Without Optimization
# end = time.perf_counter()

# print(f"Execution Time 1: {end - start:15f}")


start = time.perf_counter()
BubbleSortOptimized(data)  # With Optimization
end = time.perf_counter()
print(f"Execution Time 2: {end - start:15f}")
