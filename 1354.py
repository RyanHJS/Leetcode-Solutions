class Solution:
    def isPossible(self, target: List[int]) -> bool:

        if len(target) == 1:
            return target == [1]

        pq = [-num for num in target]
        heapq.heapify(pq)

        total = sum(target)

        while -pq[0] > 1:
            curMax = -heapq.heappop(pq)
            rest = total - curMax

            if rest == 1:
                return True

            replacement = curMax % rest

            if replacement < 1 or replacement == curMax:
                return False

            heapq.heappush(pq, -replacement)
            total = total + replacement - curMax
        
        return True