import time, random, tqdm


def InsertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j > 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp


data = [random.randint(0, 100) for _ in range(100)]
start = time.perf_counter()
InsertionSort(data)  # Without Optimization
end = time.perf_counter()
print(f"Execution Time 2: {end - start:15f}")
