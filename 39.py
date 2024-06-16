class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        All unique combinations with a sum of [target]

        Input: int array (of distinct integers) - candidates, int - target
        Output: int array of arrays - ans (may return the combinations in any order)

        Example:
            [2,3,6,7], target = 7

            Ans - [[2,2,3], [7]] 
            May use the same number an unlimited number of times

            [2,3,5], target = 8

            Ans - [[2,2,2,2], [2,3,3], [3,5]]
        '''
        ans = []
        count = Counter(candidates)
        print(count)

        cur = []
        curSum = [0]
        def dfs(i):
            if curSum[0] == target:
                ans.append(cur.copy())
                return
            if i >= len(candidates) or curSum[0] > target:
                return
            
            cur.append(candidates[i])
            curSum[0] += candidates[i]
            dfs(i)

            cur.pop()
            curSum[0] -= candidates[i]
            dfs(i+1)
        
        dfs(0)
        return ans
