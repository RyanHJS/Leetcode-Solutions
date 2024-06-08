class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-weight for weight in stones]
        heapq.heapify(pq)

        while len(pq) > 1:
            # pop twice
            y = -heapq.heappop(pq)
            x = -heapq.heappop(pq)

            if x != y:
                y -= x
                heapq.heappush(pq, -y)
            
        return -pq[0] if pq else 0
