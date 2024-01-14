class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def getIndexValue(head,index):
    iterator = head
    for i in range(1, index):
        print(iterator.data)
        iterator = iterator.next
        if iterator == None: return None
    return iterator.data
