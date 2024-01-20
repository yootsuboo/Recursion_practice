class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def palindromeLinkedList(head):
    stack = []



'''
- headからstackで値を格納
- headとstackの真ん中までを比較
- 値がすべて同じならtrue
- 違えば即false
'''
