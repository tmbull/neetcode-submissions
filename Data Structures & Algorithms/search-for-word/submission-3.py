class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # basic approach:
        # create an index into word
        # find the current char in the board
        # if found, look at neighboring chars
        # if not found, backtrack
        def dfs(i, r, c, visited):
            print(f"{i} {r} {c}")
            if (r < 0 or r >= len(board) or
                c < 0 or c >= len(board[0])):
                return False
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            visited.add((r,c))
            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for dr, dc in directions:
                if ((dr,dc) not in visited and
                    dfs(i+1, dr, dc, visited)):
                    return True
            visited.remove((r,c))
            return False
                    
        # board=[["A","B","C","E"],
        #         ["S","F","E","S"]
        #         ,["A","D","E","E"]]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(0, r, c, set()):
                    return True

        return False
