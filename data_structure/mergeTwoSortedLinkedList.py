class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeTwoSortedLinkedLists(head1, head2):
    # リストの先頭に0が入ったダミーを作成
    dummy = SinglyLinkedListNode(0)
    tail = dummy

    while True:
        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break

        if head1.data <= head2.data:
            # head1の値のほうが小さかったらteil.nextにhead1を入れてhed1を次へ
            tail.next = head1
            head1 = head1.next
        else:
            tail.next  = head2
            head2 = head2.next

        # tailの末尾を次に進めて次のループ
        tail = tail.next

    return dummy.next

