# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # to serialize, do BFS. add results to array
        # ex. [1, 2, 3, null, null, 4, 5]
        # 1,2,3,n,n,4,5,n,n,n,n
        q = deque()
        q.append(root)

        results = []
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    results.append(str(curr.val))
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    results.append("n")
        print(results)
        return ",".join(results)

    def toNode(self, data: str) -> Optional[TreeNode]:
        if data == "n":
            return None
        else:
            return TreeNode(int(data))
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # to deserialize, push onto a stack
        # 1
        # [1] [2 3]
        # [2 3] [n n 4 5]
        nodes = [self.toNode(s) for s in data.split(",")]
        print(nodes)
        q = deque()
        q.append(nodes[0])
        i = 1
        while q:
            for j in range(len(q)):
                curr = q.popleft()
                if not curr:
                    continue
                curr.left = nodes[i]
                i += 1
                curr.right = nodes[i]
                i += 1
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return nodes[0]
