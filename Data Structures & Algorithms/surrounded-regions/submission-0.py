class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # similar to num islands problem
        # iterate rows and cols
        # when an island is encountered in the middle of the board
            # map the island
            # if it does not touch an edge, set it to x's
        rows = len(board)
        cols = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            for dr, dc in directions:
                dfs(dr + r, dc + c)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(1, cols - 1):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

                    
