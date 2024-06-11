class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque() # [count, nextTime]
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                curLargest = heapq.heappop(maxHeap) + 1
                if curLargest:
                    nextAvailableTime = time + n
                    q.append([curLargest, nextAvailableTime])
            
            if q and q[0][1] == time:
                toAppend = q.popleft()
                heapq.heappush(maxHeap, toAppend[0])
        
        return time


            





