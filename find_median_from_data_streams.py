import heapq
from math import inf

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, -num)
            return

        if len(self.max_heap) <= len(self.min_heap):
            if num > self.min_heap[0]:
                x = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -x)
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        else:
            if num < -self.max_heap[0]:
                x = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, x)
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2
        else:
            return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
