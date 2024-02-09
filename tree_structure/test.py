import math
import copy 

class HeapLibrary:

    @staticmethod
    def buildMaxHeap(arr):
        mid = HeapLibrary.parent(len(arr)-1)

        for i in range(mid, -1, -1):
            HeapLibrary.maxHeapify(arr, len(arr)-1, i)

    @staticmethod
    def maxHeapify(arr, heapEnd, i):
        l = HeapLibrary.left(i)
        r = HeapLibrary.right(i)
        biggest = i

        if l <= heapEnd and arr[l] > arr[biggest]: biggest = l
        if r <= heapEnd and arr[r] > arr[biggest]: biggest = r
        
        if i != biggest:
            temp = arr[i]
            arr[i] = arr[biggest]
            arr[biggest] = temp

            return HeapLibrary.maxHeapify(arr, heapEnd, biggest) 

    @staticmethod
    def left(i):
        return i*2+1

    @staticmethod
    def right(i):
        return i*2+2

    @staticmethod
    def parent(i):
        return math.floor((i-1)/2)

class PriorityQueue:
    
    def __init__(self, arr):
        self.maxHeap = copy.deepcopy(arr)
        HeapLibrary.buildMaxHeap(self.maxHeap)
    
    def top(self):
        return self.maxHeap[0]
    
    def pop(self):
        popped = self.maxHeap[0]
        self.maxHeap[0] = self.maxHeap[len(self.maxHeap) -1]
        self.maxHeap.pop()
        HeapLibrary.maxHeapify(self.maxHeap, len(self.maxHeap)-1, 0)
        return popped

    # ここから開発してください。
    # insert      
    def insert(self, key):
        self.maxHeap.append(key)
        index = len(self.maxHeap) - 1
        parent = HeapLibrary.parent(index)

        while parent >= 0 and self.maxHeap[parent] < key:
            temp = self.maxHeap[index]
            self.maxHeap[index] = self.maxHeap[parent]
            self.maxHeap[parent] = temp
            index = parent
            parent = parent(index)

     
pq = PriorityQueue([2,3,43,2,53,6,75,10])
print(pq.maxHeap)
pq.insert(5)
print(pq.maxHeap)
pq.insert(5)
print(pq.maxHeap)
pq.insert(79)
print(pq.maxHeap)
pq.pop()
print(pq.maxHeap)
