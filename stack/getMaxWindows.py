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

    def peekBack(self):
        if self.tail is None: return None
        return self.tail.data

    def enqueueFront(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
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
        if self.head is None: return None
        temp = self.head
        self.head = self.head.next
        if self.head is not None: 
            self.head.prev = None
        else: self.tail = None

        return temp.data

    def dequeueBack(self):
        if self.tail is None: return None
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else: self.head = None

        return temp.data

def getMaxWindows(arr, k):
    if k > len(arr): return []
    res = []
    # indexを入れる箱
    deque = Deque()

    for i, num in enumerate(arr[:k]):
        # なぜarr[]にpeekBack()を入れているのかわからない??
        # dequeにはnumではなくてindexが入っているからOK
        while deque.peekBack() is not None and arr[deque.peekBack()] <= num:
            deque.dequeueBack()
        deque.enqueueBack(i)

    print(deque.peekFront())

    # arrのk番目から最後までループする。スタートはk
    for i, num in enumerate(arr[k:],k):
        res.append(arr[deque.peekFront()])
        while deque.peekFront() is not None and deque.peekFront() <= i-k:
            deque.dequeueFront()
        while deque.peekBack() is not None and arr[deque.peekBack()] <= num:
            deque.dequeueBack()
        deque.enqueueBack(i)

    res.append(arr[deque.peekFront()])

    return res


print(getMaxWindows([34,35,64,34,10,2,14,5,353,23,35,63,23], 4))


