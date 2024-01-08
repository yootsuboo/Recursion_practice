import math

def mergeSort(arr):
    return mergeSortHelper(arr, 0, len(arr) - 1)

def mergeSortHelper(arr, start, end):
    if start == end: return [arr[start]]

    middle = math.floor((start + end) / 2)
    leftArr = mergeSortHelper(arr, start, middle)
    rightArr = mergeSortHelper(arr, middle + 1, end)

    leftArr.append(math.inf)
    rightArr.append(math.inf)


    length = len(leftArr) + len(rightArr) - 2
    leftIndex = 0
    rightIndex = 0

    merged = []

    while leftIndex + rightIndex < length:
        if leftArr[leftIndex] <= rightArr[rightIndex]:
            merged.append(leftArr[leftIndex])
            leftIndex += 1

        else:
            merged.append(rightArr[rightIndex])
            rightIndex += 1

    return merged
