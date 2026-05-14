class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # initialize board to all '.'. 
        # A queen can be placed if:
            # There is no queen with the same row or col coordinate
            # There is no other queen on the same diagonal 
        # Brute force
            # place a queen, invalidate all associated places, increment counter
            # attempt to place another queen
                # if no spot is found, backtrack to previous state
                # if a spot is found, invalidate all associated palces, increment counter
        
        def placeQueen(placed, r, c):
            for pr, pc in placed:
                if pr == r or pc == c or (abs(pr - r) == abs(pc - c)):
                    return False
            return True

        placed = set()
        res = []
        board = [['.'] * n for i in range(n)]
        def backtrack(r):
            print(placed)
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if not placeQueen(placed, r, c):
                    continue
                
                placed.add((r, c))
                board[r][c] = 'Q'
                backtrack(r + 1)
                placed.remove((r,c))
                board[r][c] = '.'

        backtrack(0)
        return res
                    
