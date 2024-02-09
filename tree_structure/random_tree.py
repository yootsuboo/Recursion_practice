import math
import random

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printInOrder(self):
        self.inOrderWalk(self)
        print("")

    def inOrderWalk(self, tRoot):
        if tRoot is not None:
            self.inOrderWalk(tRoot.left)
            print(str(tRoot.data), end=' ')
            self.inOrderWalk(tRoot.right)


class BinarySearchTree:
    def __init__(self, arrList):
        self.generateRandomBST(arrList)

    def generateRandomBST(self, arrList):
        if not arrList:
            self.root = None
        else:
            BinarySearchTree.shuffle(arrList)
            self.root = BinaryTree(arrList[0])
            for i in range(len(arrList)):
                self.insert(arrList[i])

    def insert(self, value):
        iterator = self.root
        while iterator is not None:
            if iterator.data > value and iterator.left is None:
                iterator.left = BinaryTree(value)
            elif iterator.data < value and iterator.right is None:
                iterator.right = BinaryTree(value)
            iterator = iterator.left if iterator.data > value else iterator.right


    @staticmethod
    def shuffle(list):
        for i in range(len(list)-1, -1, -1):
            j = math.floor(random.randint(0, i+1))
            [list[i], list[j]] = [list[j], list[i]]
        return list

    @staticmethod
    def maximumDepth(root):
        if root is None: return 0
        leftdepth = BinarySearchTree.maximumDepth(root.left)
        rightdepth = BinarySearchTree.maximumDepth(root.right)
        return rightdepth + 1 if rightdepth > leftdepth else leftdepth + 1

    def printSorted(self):
        if self.root is None: return
        self.root.printInOrder()

class RandomContainer:
    @staticmethod
    def generateList(size):
        list = []
        for i in range(size):
            list.append(i)
        return list

list = RandomContainer.generateList(256)
balancedBST = BinarySearchTree(list)
balancedBST.printSorted()

print(16*16)
print("MaxDepth: " + str(BinarySearchTree.maximumDepth(balancedBST.root)))

list2 = []
balancedBST2 = BinarySearchTree(list2)
balancedBST2.printSorted()
print("MaxDepth: " + str(BinarySearchTree.maximumDepth(balancedBST2.root)))

