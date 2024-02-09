class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def pop(self):
        if self.head is None: return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peek(self):
        if self.head is None: return None
        return self.head.data

def consecutiveWalk(arr):
    stack = Stack()
    stack.push(arr[0])

    for i in arr[1:]:
        if stack.peek() < i:
            while stack.peek() is not None:
                stack.pop()

        stack.push(i)

    results = []
    while stack.peek() is not None:
        results.append(stack.pop())

    return results

print(consecutiveWalk([3,4,20,45,6,4,3,5,3,2]))
