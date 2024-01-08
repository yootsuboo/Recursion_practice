import math

def sumOfArray(arr):
    return sumOfArrayHelper(arr, 0, len(arr) - 1)


def sumOfArrayHelper(arr, start, end):
    # start == end になるときがすべて分割して値が一つになったとき
    if start == end:
        return arr[start]
    # rightArrでstartに0以外を使用するのでstartも足さなくてはいけない
    mid = math.floor((start + end) / 2)

    leftArr = sumOfArrayHelper(arr, start, mid)
    rightArr = sumOfArrayHelper(arr, mid + 1, end)

    return leftArr + rightArr

arr = [2, 4, 5, 9 ,11, 13]
print(sumOfArray(arr))
