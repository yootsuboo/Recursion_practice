def consecutiveWalk(arr):
    stack = Stack()
    results = []

    stack.push(arr[0])
    for i in arr[1:]:
        if stack.peek() > i:
            while stack.peek() is not None:
                stack.pop()

        stack.push(i)

    while stack.peek() is not None:
        results.append(stack.pop())

    return results


class Item:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = self.head
        self.head = Item(data)
        self.head.next = temp

    def pop(self):
        if self.head == None: return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peek(self):
        if self.head == None: return None
        return self.head.data

