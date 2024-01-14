class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def addNextNode(self, newNode):
        tempNode = self.next
        self.next = newNode
        newNode.next = tempNode

def doubleEvenNumber(head):
    iterator = head
    index = 0

    while iterator is not None:
        currentNode = iterator
        iterator = iterator.next
        if index % 2 == 0:
            currentNode.addNextNode(SinglyLinkedListNode(currentNode.data * 2))
        index += 1

    # なぜ戻り値をheadにすることで連結リストが返されるのかわかっていない..
    return head


