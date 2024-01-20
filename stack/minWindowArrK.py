def minWindowArrK(intArr, k):
    if k > len(intArr): return []

    results = []

    deque = Deque()
    for i, num in enumerate(intArr[:k]):
        while deque.peekBack() is not None and intArr[deque.peekBack()] >= num:
            deque.dequeueBack()
        deque.enqueueBack(i)

    for i, num in enumerate(intArr[k:], k):
        results.append(intArr[deque.peekFront()])
        while deque.peekFront() is not None and deque.peekFront() <= i-k:
            deque.dequeueFront()
        while deque.peekBack() is not None and intArr[deque.peekBack()] >= num:
            deque.dequeueBack()
        deque.enqueueBack(i)

    results.append(intArr[deque.peekFront()])
    return results


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
        if self.head is None:
            return None
        return self.head.data

    def peekBack(self):
        if self.tail is None:
            return None
        return self.tail.data

    def enqueueFront(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head

        node = Node(data)
        self.head.prev = node
        node.next = self.head
        self.head = node

    def enqueueBack(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head

        else:
            node = Node(data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def dequeueFront(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is not None: self.head.prev = None
        else:
            self.tail = None
        return temp.data

    def dequeueBack(self):
        if self.tail is None: return None
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return temp.data



