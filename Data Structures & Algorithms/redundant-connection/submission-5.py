class UnionFind:
    def __init__(self, edges):
        self.par = [i for i in range(edges + 1)]
        self.rank = [1] * (edges + 1)

    def findParent(self, n):
        par = self.par[n]
        while par != self.par[par]:
            self.par[par] = self.par[self.par[par]]
            par = self.par[par]

        return par
    
    def union(self, n1, n2):
        par1, par2 = self.findParent(n1), self.findParent(n2)

        if par1 == par2:
            return False

        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += self.rank[par2]
        else:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]
        return True

        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find
        # union edges
        # if a cycle is detected, return nodes
        uf = UnionFind(len(edges))
        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return [n1, n2]

        return None