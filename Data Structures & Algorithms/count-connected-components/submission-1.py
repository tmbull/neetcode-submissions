class UnionFind:
    def __init__(self, n):
        self.par = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}

    def findParent(self, n):
        res = n
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res] 
        
        return res

    def union(self, x, y):
        px, py = self.findParent(x), self.findParent(y)
        if px == py:
            return 0

        if self.rank[py] > self.rank[px]:
            self.par[px] = py
            self.rank[py] += self.rank[px]
        else:
            self.par[py] = px
            self.rank[px] += self.rank[py]

        return 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # a connected component is a group of nodes that are connected together
        # num components is the number of distinct groups
        uf = UnionFind(n)
        res = n
        for x, y in edges:
            res -= uf.union(x, y)

        return res
