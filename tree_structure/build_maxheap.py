import math

def heapsort(intArr):
    arr = builMaxHeap(intArr)

    heapEnd = len(arr) - 1
    while heapEnd > 0:
        temp = arr[heapEnd]
        arr[heapEnd] = arr[0]
        arr[0] = temp

        heapEnd -= 1
        maxHeapify(arr, heapEnd, 0)

    return arr

def builMaxHeap(arr):
    middle = parent(len(arr))
    for i in range(middle, -1, -1):
        maxHeapify(arr, len(arr) -1, i)
    return arr

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return math.floor((i - 1) / 2)

def maxHeapify(arr, heapEnd, i):
    l = left(i)
    r = right(i)

    biggest = i
    if l <= heapEnd and arr[l] > arr[biggest]:
        biggest = l
    if r <= heapEnd and arr[r] > arr[biggest]:
        biggest = r
    if biggest != i:
        temp = arr[i]
        arr[i] = arr[biggest]
        arr[biggest] = temp
        maxHeapify(arr, heapEnd, biggest)

