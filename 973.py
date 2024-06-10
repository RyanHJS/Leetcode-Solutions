class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Input: int array
        Output: array of int array(s)

        Goal: find the k closest points to origin

        Closest:
        [1,3], [-2,2]
        Find the distance to origin (0,0)

        sqrt[(1-0)^2 + (3-0)^2] = sqrt(10)
        sqrt[(-2-0)^2 + (2-0)^2] = sqrt(8)

        Store in a heap (min heap)
        Return k closest
        '''

        distance = []
        heapq.heapify(distance)

        for point in points:
            x1, y1 = point
            x2, y2 = 0, 0

            curDistanceToOrigin = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            heapq.heappush(distance, (curDistanceToOrigin, point))
        
        ans = []

        for i in range(k):
            ans.append(heapq.heappop(distance)[1])
        
        return ans