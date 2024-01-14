class Item:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, node):
        self.head = node


item1 = Item(7)
item2 = Item(99)
item3 = Item(45)

item1.next = item2
item2.next = item3

numList = SinglyLinkedList(item1)

currentNode = numList.head
while currentNode is not None:
    print(currentNode.data)
    currentNode = currentNode.next
