class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Input: m x n grid - board, string - word

        Goal: find if word exists in board, letters must be hironztally or vertically neighbouring

        Output: true/false
        
        1. If board was given as a string
            Find if every letter in word has been used in board
                Use a dictionary to get the count of letters
                    Iterate through board and decrement count
                        If all counts in word == 0, then return True
        
        2. DFS - row x cols (WITHIN BOUNDS)
            Move rows +/- 1
            Move cols +/- 1
        
        Backtracking 
            At every letter: 4 choices
            row + 1
            row - 1
            col + 1
            col - 1
        '''
        seen = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, i):
            if i == len(word):
                return True
            if row >= ROWS or row < 0 or col >= COLS or col < 0 or (row, col) in seen or word[i] != board[row][col]:
                return False

            seen.add((row, col))

            res = (dfs(row+1, col, i+1) or 
            dfs(row-1, col, i+1) or
            dfs(row, col+1, i+1) or
            dfs(row, col-1, i+1))

            seen.remove((row, col))

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False