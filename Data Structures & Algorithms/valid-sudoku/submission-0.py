class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force
            # check rows, cols, and submatrices
            # subs:
            # 0 1 2 vertical = row // 3 
            # 3 4 5 horizontal = col // 3
            # 6 7 8 idx = vertical*3 + horizontal 
            # 
            # 3+0 3+1
        SIZE = 9
        rows = [set() for i in range(SIZE)]
        cols = [set() for i in range(SIZE)]
        subs = [set() for i in range(SIZE)]

        for r in range(SIZE):
            for c in range(SIZE):
                v = r // 3
                h = c // 3
                sub = (v*3) + h
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows[r] or val in cols[c] or val in subs[sub]:
                    print(f"v: {val} r: {r}:{rows[r]} c: {c}:{cols[c]} s: {sub}:{subs[sub]}")
                    return False
                rows[r].add(val)
                cols[c].add(val)
                subs[sub].add(val)

        return True