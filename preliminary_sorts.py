def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_key = arr[i]
        for j in range(i, -1, -1):
            if current_key < arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = current_key
    return arr


def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        current_key = arr[i]
        for j in range(i, -1, -1):
            if current_key > arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = current_key
    return arr


def selection_sort(arr):
    for i in range(0, len(arr)):
        min = arr[i]
        min_pointer = i
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_pointer = j
        temp = arr[i]
        arr[i] = min
        arr[min_pointer] = temp

    return arr


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) -i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr
