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

# ここから書きましょう

class PriorityQueue:
   def __init__(self, arr):
      self.arr = copy.deepcopy(arr)
      HeapLibrary.buildMaxHeap(self.arr)
   
   def top(self):
      return self.arr[0]
   
pq1 = PriorityQueue([2,3,43,2,53,6,75,10])
print(pq1.top())
pq2 = PriorityQueue([3,12,0,2,9,1,65,32])
print(pq2.top())
pq3 = PriorityQueue([1,2,3,4,8,2,1,9,7,3,4])
print(pq3.top())
