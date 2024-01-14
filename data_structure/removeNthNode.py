class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeNthNode(head,n):
    iterator = head
    index = 0

    while iterator is not None:
        iterator = iterator.next
        index += 1

    
    if n == 0 or index < n: 
        return head

    if index == n:
        head = head.next
        return head

    iterator = head
    for _ in range(index - n - 1):
        iterator = iterator.next
    iterator.next = iterator.next.next
    return head
