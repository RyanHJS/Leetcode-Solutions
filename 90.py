class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Input: int array - nums (may contain duplicates)
        Output: array of arrays - ans (power set, all possible subsets)

        Goal: find all possible subsets, without duplicates

        DFS Backtracking:
            Decision - include, or not include the current
        '''
        ans = []

        cur = []

        nums.sort()

        def dfs(i):
            if i >= len(nums):
                if cur not in ans:
                    ans.append(cur[::])
                return

            cur.append(nums[i])
            dfs(i+1)

            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return ans
