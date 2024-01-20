class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
        self.size += 1

    def pop(self):
        if self.head is None: return None
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp.data

    def peek(self):
        if self.head is None: return None
        return self.head.data

    def __len__(self):
        return self.size


    def toList(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return ','.join(map(str, result[::-1]))


def diceStreakGamble(player1,player2,player3,player4):
    totalAmount = []
    players = [player1, player2, player3, player4]
    allStack = []
    
    for player in players:
        stack = Stack()
        stack.push(player[0])
        for i in range(1, len(player)):
            if stack.peek() < player[i]:
                stack.push(player[i])
            else:
                while stack.head is not None:
                    stack.pop()
                stack.push(player[i])
        allStack.append(stack)
        totalAmount.append(len(stack) * 4)

    maxIndex = totalAmount.index(max(totalAmount))
    winPlayer = maxIndex + 1
    return "Winner: Player " + str(winPlayer) + " won $" + str(totalAmount[maxIndex]) + " by rolling[" + allStack[maxIndex].toList() + "]"


