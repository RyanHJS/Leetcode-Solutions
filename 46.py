class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        input: int array - nums (distinct integers)
        output: array of arrays - ans (can be in any order)

        goal: return all possible permutations
            permutation must include all elements
        '''

        def dfs(path, used, res):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for letter in nums:
                if letter in used and used[letter]:
                    continue
                path.append(letter)
                used[letter] = True
                dfs(path, used, res)

                path.pop()
                used[letter] = False
        
        res = []
        dfs([], {}, res)
        return res