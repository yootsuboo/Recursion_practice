class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(head):
    # 連結リストの最後のNoneとは別のNone
    reverseHead = None
    current = head
    while current is not None:
        nextNode = current.next    # reverseHead = None, current = head[0] current.next = head[1]
        current.next = reverseHead # current.next = None
        reverseHead = current      # reverseHead = head[0]
        current = nextNode         # current head[1]
    return reverseHead


