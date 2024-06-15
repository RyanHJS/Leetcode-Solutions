class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Subset:

        Input: int array - nums
        Output: int set - ans

        Goal: find all possible subsets
            The empty set is always a subset 
            The set itself is always a subset

        Example:
            [1,2,3]
            [], [1], [2], [3], [1,2], [1,3], [1,2,3], [2,3]
        
        Decision Tree?
            What is the decision? To add or not to add the current node/element/number/etc....
            
            []: 1 
            [1], []: 2 (ADD OR 1, or [])
            [1,2], [1], [2], []: 4 (ADD OR 2, or [])
            [1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []: 8 (ADD OR 3, or [])

        '''
        res = []

        cur = []
        # i for index
        def dfs(i):
            if i >= len(nums):
                # should not iterate anymore
                # copy the current iteration to our answer
                res.append(cur.copy())
                return
            
            # decisions #1, to include the current element
            dfs(i+1)
            # decisions #2, NOT to include the current element
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
        
        dfs(0)
        return res