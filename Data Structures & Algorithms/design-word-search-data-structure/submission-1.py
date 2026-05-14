class Node:
    def __init__(self):
        self.dictionary = [None] * 26
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            ch_idx = ord(word[i]) - ord('a')
            if not curr.dictionary[ch_idx]:
                curr.dictionary[ch_idx] = Node()
            curr = curr.dictionary[ch_idx]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(curr, i):
            while curr and i < len(word):
                if word[i] == '.':
                    # check all
                    for idx in range(26):
                        if dfs(curr.dictionary[idx], i + 1):
                            return True
                    return False
                else:
                    ch_idx = ord(word[i]) - ord('a')
                    if not curr.dictionary[ch_idx]:
                        return False
                    curr = curr.dictionary[ch_idx]
                    i += 1
            return curr and curr.is_word

        return dfs(self.root, 0)

        
