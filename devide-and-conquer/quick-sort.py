def quickSort(arr):
    # ベースケース: 配列の長さが1以下の場合そのまま値を返す
    if len(arr) <= 1:
        return arr

    # 配列を分割するための基準点を作成
    pivot = arr[len(arr) // 2]
    # pivotより値が小さい配列の作成
    left = [x for x in arr if x < pivot]
    # pivotと同じ値の配列の作成
    middle = [x for x in arr if x == pivot]
    # pivotより値が大きい配列の作成
    right = [x for x in arr if x > pivot]

    # leftとrightは再帰的に繰り返し値を統合
    return quickSort(left) + middle + quickSort(right)


