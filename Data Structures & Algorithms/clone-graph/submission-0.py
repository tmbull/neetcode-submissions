"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.clone(node, {})
    def clone(self, node: Optional['Node'], visited: dict[Node, Node]) -> Optional['Node']:
        # DFS, create a node and then iterate over children nodes
        # continue until there are no more children
        if not node:
            return None

        if node in visited:
            return visited[node]

        root = Node(node.val)
        visited[node] = root

        if node.neighbors:
            root.neighbors = []
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    root.neighbors.append(self.clone(neighbor, visited))

        return root