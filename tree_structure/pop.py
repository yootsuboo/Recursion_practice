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
   
   def pop(self):
      poped = self.arr[0]
      self.arr[0] = self.arr[len(self.arr) - 1]
      self.arr.pop(-1)
      HeapLibrary.maxHeapify(self.arr, len(self.arr) - 1, 0)
      return poped

pq = PriorityQueue([2,3,43,2,53,6,75,10])
print(pq.pop())
print(pq.pop())
print(pq.pop())
print(pq.pop())
