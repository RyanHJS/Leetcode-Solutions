class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        Input: string - s
        Goal: Partition input such that every substring is a palindrome
        Output: array of arrays - all possible palindrome partitioning of s
            Each partition must contain all of s

        Example:
            'aab'
            a, a, b
            aa, b

        1. Have function to check if palindrome
                p[::] == p[::-1]
        2. Generate all possible partionings and check if each is a palindrome

        Backtracking:
            Include, or not include?

        '''

        ans = []
        cur = []

        def dfs(i):
            if i >= len(s):
                ans.append(cur[::])
                return

            # Iterate over all possible combinations from the starting index
                # if a is a palindrome, add to cur and explore everything after a (a>ab, b)
                    # Then backtrack by popping the last operation and check (aa, b, aab)
            for j in range(i, len(s)):
                print(f'In for loop {s[i:j+1]}')
                if self.isPalindrome(s[i:j+1]):
                    cur.append(s[i:j+1])
                    dfs(j+1)
                    cur.pop()
        
        dfs(0)
        return ans

    def isPalindrome(self, s):
        return s == s[::-1]


            
            