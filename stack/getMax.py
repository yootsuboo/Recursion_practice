def getMax(arr):
    deque = Deque()
    deque.enqueueFront(arr[0])

    for i in arr[1:]:
        if i > deque.peekFront():
            deque.enqueueFront(i)
        else:
            deque.enqueueBack(i)
    
    return deque.peekFront()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self):
        if self.head is None: return None
        return self.head.data

    def enqueueFront(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev

    def enqueueBack(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

