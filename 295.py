class MedianFinder:

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []

    def addNum(self, num: int) -> None:
        if self.rightHeap and num > self.rightHeap[0]:
            heapq.heappush(self.rightHeap, num)
        else:
            heapq.heappush(self.leftHeap, -1 * num)

        if len(self.leftHeap) > len(self.rightHeap) + 1:
            leftMax = -1 * heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, leftMax)
        if len(self.rightHeap) > len(self.leftHeap) + 1:
            rightMin = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, -1 * rightMin)

    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return -1 * self.leftHeap[0]
        elif len(self.rightHeap) > len(self.leftHeap):
            return self.rightHeap[0]
        else:
            leftMax, rightMin = -1 * self.leftHeap[0], self.rightHeap[0]
            return (leftMax + rightMin) / 2.0



        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

'''
Example:
    [2,3,4] - ODD - median 3
    [2,3] - EVEN - median (2+3) / 2 = 2.5

    Use 2 heaps

    left stream
    []

    right stream
    []

    What are the conditions to add to the left stream?
    What are the conditions to add to the right stream?

    [1] [5 9 99 999 9999]

    if num > leftLargest and len(rightHeap) < len(leftHeap):
        ADD TO RIGHT
    else:
        ADD TO LEFT

    left should be a max heap
    right should be a min heap

    GOAL:
        if even:
            pop the largest in left and min in right...
        if odd:
            pop the first element in the longer heap
'''