# 二分ヒープ（binary heap）は特別な種類の完全二分木で、特定のプロパティを満たす木構造です。
# この二分ヒープの特性は、任意の親ノードの値がその子ノードの値と等しく、
# またはそれより大きい（または小さい）ことです。
# これにより、最大ヒープ（親ノードが子ノードよりも値が大きい）または
# 最小ヒープ（親ノードが子ノードよりも値が小さい）が形成されます。


# 二分ヒープは完全二分木であることから、配列のインデックスを i とすると、次のような規則があります。
# 
# i 番目のノードの左の子ノード: left(i) = 2i + 1
# i 番目のノードの右の子ノード: right(i) = 2i + 2
# i 番目のノードの親ノード: parent(i) = floor((i-1) / 2)


# Heapクラスは二分ヒープを操作するためのクラスです。
import math

class Heap:
    @staticmethod
    def left(i):
        # 左の子ノードのインデックスを計算します。0から始まるインデックスを使用します。
        return 2*i + 1

    @staticmethod
    def right(i):
        # 右の子ノードのインデックスを計算します。0から始まるインデックスを使用します。
        return 2*i + 2

    @staticmethod
    def parent(i):
        return math.floor((i-1)/2)

    @staticmethod
    # 最大ヒープを構築します。つまり、あるノードとその子ノードが条件を満たさない場合に、そのノードを再配置します。
    def maxHeapify(arr, heapEnd, i):
        # この条件は、親ノードがその子ノードよりも大きいか等しいというものです。
        # 左の子ノードのインデックスを取得します。
        l = Heap.left(i)
        # 右の子ノードのインデックスを取得します。
        r = Heap.right(i)

        # 最大値のインデックスを保存します。初期値は親ノードのインデックスです。
        biggest = i
        # 子ノードが存在し、それが親ノードよりも大きい場合、最大値のインデックスを更新します。
        if l < heapEnd and arr[l] > arr[biggest]: biggest = l
        if r < heapEnd and arr[r] > arr[biggest]: biggest = r

        # 親ノードが最大値でなければ、親ノードと最大値を交換し、再度ヒープ構築を行います。
        if biggest != i:
            temp = arr[i]
            arr[i] = arr[biggest]
            arr[biggest] = temp
            Heap.maxHeapify(arr, heapEnd, biggest)

    # buildMaxHeapを実装します。
    @staticmethod 
    def buildMaxHeap(arr):
        middle = Heap.parent(len(arr))
        # 最後の葉ノードの親ノードから根ノードまで maxHeapfy します。
        for i in range(middle, -1, -1):
            Heap.maxHeapify(arr, len(arr)-1, i)
          
    # ヒープソートを実装します。
    @staticmethod
    def heapSort(arr):
        # まず、配列arrをヒープ構造に変換します。このためにbuildMaxHeapメソッドを使用します。
        # ヒープ構造とは、特定のプロパティを持つ完全二分木のことを指します。
        # 最大ヒープの場合、すべての親ノードはその子ノードより大きい値を持ちます。
        Heap.buildMaxHeap(arr)

        # ヒープサイズを追跡するためにheapEndという変数を作り、最初は配列の最後の要素を指すようにします。
        heapEnd = len(arr) - 1
        while(heapEnd > 0):
            # ここでは、ヒープの根（最大値）とヒープの最後の要素heapEndを交換します。
            # これにより、最大の要素が配列の正しい位置、つまり末尾に移動します。
            temp = arr[heapEnd]
            arr[heapEnd] = arr[0]
            arr[0] = temp

            # 交換が完了したので、ヒープの終端を一つ左（前）に移動します。
            # これは、現在の最大値（元々の根）が正しい場所に移動したため、それを無視できることを意味します。
            heapEnd -= 1

            # ヒープの根を変更したため、ヒープの性質が破壊されている可能性があります。
            # したがって、maxHeapifyメソッドを使って再度ヒープ性質を満たすように調整します。
            Heap.maxHeapify(arr, heapEnd, 0)


heap1 = [2,42,11,30,10,7,6,5,9]
print(heap1)
Heap.heapSort(heap1)
print(heap1) # 昇順にソートされました。

heap2 = [56,4,51,10,12,5,12,4,6,5]
print(heap2)
Heap.heapSort(heap2)
print(heap2)
