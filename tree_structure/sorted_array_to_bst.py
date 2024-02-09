import math

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        # BinaryTreeのノードが持つ値をセットします。
        self.data = data
        # BinaryTreeのノードが持つ左側の子ノードへの参照をセットします。
        # 子ノードが存在しない場合、デフォルトはNoneです。
        self.left = left
        # BinaryTreeのノードが持つ右側の子ノードへの参照をセットします。
        # 子ノードが存在しない場合、デフォルトはNoneです。
        self.right = right

# 与えられた配列をバランスの取れた二分探索木に変換するヘルパー関数
def sortedArrayToBSTHelper(arr, start, end):
    # 配列の長さが1の場合（startとendが同じ位置にある場合）、新しいノードを作成します。
    # この新しいノードのデータは配列のその位置の値となります。
    if start == end: return BinaryTree(arr[start], None, None)

    # 中央のインデックスを求めます。これが新しいノードの値となります。
    # 中央より後ろのインデックスは葉ノードなので探索しなくていい
    mid = math.floor((start+end)/2)

    left = None
    # 配列の左半分を再帰的に処理します。これが新しいノードの左側の子ノードとなります。
    if mid-1 >= start:
        left = sortedArrayToBSTHelper(arr, start, mid-1)

    right = None
    # 配列の右半分を再帰的に処理します。これが新しいノードの右側の子ノードとなります。
    if mid+1 <= end: 
        right = sortedArrayToBSTHelper(arr, mid+1, end)

    # 左右の子ノードを持つ新しい根ノードを作成します。
    root = BinaryTree(arr[mid], left, right)
    return root

# ソートされた配列をバランスの取れた二分探索木に変換する関数
def sortedArrayToBST(nums):
    # 空の配列が与えられた場合、二分探索木を作成する要素が存在しないため、Noneを返します。
    if len(nums) == 0: return None
    # ヘルパー関数を呼び出して、配列を二分探索木に変換します。配列の最初のインデックスと最後のインデックスを引数に渡します。
    return sortedArrayToBSTHelper(nums, 0, len(nums)-1)

# ソート済み配列をバランスの取れた二分探索木に変換します。
# この例では、[1,2,3,4,5,6,7,8,9,10,11]という数値リストがバランスの取れた二分探索木に変換されます。
balancedBST = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10,11])

# 生成されたバランスの取れた二分探索木の根ノード（balancedBST）を表示します。
print(balancedBST)
