class Trie:
    def __init__(self):
        self.prefixes: dict[str, Trie] = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.trie = Trie()

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.prefixes:
                curr.prefixes[c] = Trie()
            curr = curr.prefixes[c]
        curr.word = True


    def search(self, word: str) -> bool:
        result = self.find(word)
        return result.word
        

    def find(self, word:str) -> Optional[Trie]:
        curr = self.trie
        for c in word:
            if c not in curr.prefixes:
                return None
            else:
                curr = curr.prefixes[c]

        return curr
        

    def startsWith(self, prefix: str) -> bool:
        result = self.find(prefix)

        return result is not None

        
        