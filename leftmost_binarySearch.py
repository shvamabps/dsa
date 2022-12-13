def first(arr, low, high, key, size):
    if high >= low:
        mid = low + (high - low) // 2
        if ((mid == 0) or key > arr[mid - 1]) and arr[mid] == key:
            return mid
        elif key > arr[mid]:
            return first(arr, mid + 1, high, key, size)
        else:
            return first(arr, low, mid - 1, key, size)
    return low


def last(arr, low, high, key, size):
    if high >= low:
        mid = low + (high - low) // 2
        if ((mid == size - 1) or key < arr[mid - 1]) and arr[mid] == key:
            return mid
        elif key < arr[mid]:
            return last(arr, low, mid - 1, key, size)
        else:
            return last(arr, mid + 1, high, key, size)
    return low


a = [1, 2, 3, 5, 5, 7, 7, 8, 8, 9, 9]
size = len(a)
key = 23
print(size)
print(first(a, 0, size - 1, key, size))
print(last(a, 0, size - 1, key, size))
