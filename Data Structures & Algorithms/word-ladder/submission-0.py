class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # generate adjacency list of words -> words with < 1 char diff
        if endWord not in wordList:
            return 0
        neighbors = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(beginWord)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)

        q = deque([beginWord])
        visit = set([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
            res += 1

        return 0
