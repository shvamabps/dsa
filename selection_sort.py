def SelectionSort(a):
    for i in range(len(a)):
        small = i
        for j in range(i + 1, len(a)):
            if a[small] > a[j]:
                small = j
        a[i], a[small] = a[small], a[i]
        print("array", a, "\n")


data = [4, 5, 6, 2, 43, 9, 1]
print("data", data, "\n")
SelectionSort(data)
