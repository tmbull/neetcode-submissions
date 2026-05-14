class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # original find word algorithm backtracks when a char in a word cannot be found
        # visited chars is maintained for the current search
        # cells can be re-used in words, but not within a word, so the backtracking here should be the same
        # visited should be reset whenever searching for a new word
        rows = len(board)
        cols = len(board[0])

        def dfs(word, visited, i, r, c):
            if i == len(word):
                return True
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or
                (r, c) in visited or
                word[i] != board[r][c]):
                return False
            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            visited.add((r, c))
            for (dr, dc) in directions:
                if dfs(word, visited, i + 1, dr, dc):
                    return True
            return False

        def find_word(word) -> bool:
            for r in range(rows):
                for c in range(cols):
                    if dfs(word, set(), 0, r, c):
                        return True

            return False

        results = []
        for word in words:
            if find_word(word):
                results.append(word)
        return results