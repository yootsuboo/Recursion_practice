import math

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    # 'printInOrder'関数を定義します。この関数は、二分木の各ノードのデータを間順走査で表示します。
    def printInOrder(self):
        # 'inOrderWalk'関数を使って、二分木を間順走査します。起点となるノードは二分木のルートノードとします。
        self.inOrderWalk(self)
        # 全てのノードのデータを表示し終わったら、改行を出力します。
        print("")

    # 'inOrderWalk'関数を定義します。この関数は、指定したノードから始まる部分木を間順走査します。
    def inOrderWalk(self, tRoot):
        # 指定したノードがNoneでなければ、以下の処理を行います。（Noneは通常、二分木の末端を表す）
        if tRoot is not None:
            # 左部分木を間順走査します。再帰的にこの関数を呼び出すことで、巡回を行います。
            self.inOrderWalk(tRoot.left)
            # 左部分木を巡回した後、自ノードのデータを出力します。出力の末尾にスペースを追加することで、データが分かりやすく表示されます。
            print(str(tRoot.data), end=' ')
            # 最後に、右部分木を間順走査します。これも再帰的にこの関数を呼び出すことで、巡回を行います。
            self.inOrderWalk(tRoot.right)

class BinarySearchTree:
    def __init__(self, arrList):
        sortedList = sorted(arrList)
        self.root = BinarySearchTree.sortedArrayToBST(sortedList)

    @staticmethod
    def sortedArrayToBST(array):
        if len(array) == 0: return None
        return BinarySearchTree.sortedArrayToBSTHelper(array, 0, len(array)-1)

    @staticmethod
    def sortedArrayToBSTHelper(arr, start, end):
        if start == end: return BinaryTree(arr[start], None, None);

        mid = math.floor((start+end)/2)

        left = None;
        if mid-1 >= start: left = BinarySearchTree.sortedArrayToBSTHelper(arr, start, mid-1)

        right = None
        if mid+1 <= end: right = BinarySearchTree.sortedArrayToBSTHelper(arr, mid+1, end)

        root = BinaryTree(arr[mid], left, right)
        return root

    def keyExist(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key:return True
            if iterator.data > key: iterator = iterator.left
            else: iterator = iterator.right

        return False

    def search(self, key):
        iterator = self.root
        while iterator is not None:
            if iterator.data == key: return iterator
            if iterator.data > key: iterator = iterator.left
            else: iterator = iterator.right

        return None

    def printSorted(self):
        self.root.printInOrder()

balancedBST = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11])
balancedBST2 = BinarySearchTree([4,43,36,46,32,7,97,95,34,8,96,35,85,1010,232])
balancedBST.printSorted()
balancedBST2.printSorted()
