# def shipmentVolumePackages(packages):
#     arr = packages
#     arr.sort(reverse=True)
#     q = Queue()
#     while arr is not []:
#         number = arr.pop() + arr.pop()
#         q.enqueue(number)
#     print(q)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def enqueue(self, data):
#         if self.head is None: return None
#         self.head = Node(data)
#         self.tail = self.head

#     def dequeue(self):
#         if self.head is None: return None
#         temp = self.head
#         self.head = self.head.next
#         if self.head is None: self.tail = None
#         return temp.data

def shipmentVolumePackages(packages):
    total = 0
    while len(packages) > 1:
        packages = sorted(packages)
        newPack = packages.pop(0)+ packages.pop(0)
        total += newPack
        packages.append(newPack)
        
    return total
