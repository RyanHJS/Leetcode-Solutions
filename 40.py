class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Find all unique combinations that sum up to target

        Each number may only be used once

        Do not contain unique combinations
        '''

        candidates.sort()

        ans = []
        
        def dfs(i,cur, curSum):
            if curSum == target:
                ans.append(cur[::])
                return
            if i >= len(candidates):
                return
            if candidates[i] > target or curSum > target:
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur, curSum + candidates[i])

            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, curSum)
        
        dfs(0, [], 0)
        return ans