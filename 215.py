class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Input: int array - nums, int - k
        Output: int
        Goal: find the kth largest element in the array
        '''

        pq = nums[:k]
        heapq.heapify(pq)

        for num in nums[k:]:
            if num > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, num)
        
        return pq[0]