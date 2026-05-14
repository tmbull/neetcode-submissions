class Trie:
    def __init__(self):
        self.nodes = {}
        self.is_word = False
        self.refs = 0

    def add_word(self, word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = Trie()
            curr = curr.nodes[c]
            curr.refs += 1
        curr.is_word = True

    def remove_word(self, word):
        curr = self
        curr.refs -= 1
        for c in word:
            curr = curr.nodes[c]
            curr.refs -= 1
        curr.is_word = False

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # original find word algorithm backtracks when a char in a word cannot be found
        # visited chars is maintained for the current search
        # cells can be re-used in words, but not within a word, so the backtracking here should be the same
        # visited should be reset whenever searching for a new word
        trie = Trie()
        for word in words:
            trie.add_word(word)

        # brute force is too slow. Optimization: maintain trie of found words and lookup in trie first
        rows = len(board)
        cols = len(board[0])
        results, visited = set(), set()

        def dfs(word, node, r, c):
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or
                (r, c) in visited or
                board[r][c] not in node.nodes
                or node.nodes[board[r][c]].refs < 1):
                return
            visited.add((r, c))
            node = node.nodes[board[r][c]]
            word += board[r][c]
            if node.is_word:
                results.add(word)
                trie.remove_word(word)
            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for (dr, dc) in directions:
                dfs(word, node, dr, dc)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs("", trie, r, c)

        return list(results)