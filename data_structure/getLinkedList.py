# class SinglyLinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def getLinkedList(arr):
#     res = ""
#     numList = SinglyLinkedListNode(arr[0])

#     currentNode = numList
#     for i in range(1, len(arr)):
#         currentNode.next = SinglyLinkedListNode(arr[i])
#         currentNode = currentNode.next

#     currentNode = numList
#     while currentNode is not None:
#         res = res + str(currentNode.data) + "➡"
#         currentNode = currentNode.next

#     return res + "END"

# print(getLinkedList([3,2,1,5,6,4]))

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def getLinkedList(arr):
    res = ""
    numList = SinglyLinkedListNode(arr[0])

    currentNode = numList
    for i in range(1, len(arr)):
        currentNode.next = SinglyLinkedListNode(arr[i])
        currentNode = currentNode.next

    return numList

