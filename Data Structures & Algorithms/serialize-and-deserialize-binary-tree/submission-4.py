# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # standard encoding
            # left = root * 2 + 1
            # right = root * 2 + 2
        '''
                    0
                1       2
            3       4 5     6
        7   8   9   10 11   12  13  14
        considerations: 
            compression - omit the "null" children of "null nodes"
                so we need to keep track of "valid" nodes. ex. 3 is null so 4 becomes 3, etc. 
            we should use BFS to do layer-based traversal
        '''
        if not root:
            return ""
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node is not None:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
        
        while result[-1] == "None":
            # clean up any trailing nulls at the end of the list
            result.pop()

        result = ",".join(result)
        print(result)
        return result

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        if not nodes:
            return None

        if len(nodes) == 1:
            return TreeNode(nodes[0])

        root = TreeNode(int(nodes[0]))
        index = 1
        queue = deque()
        queue.append(root)
        # don't iterate through the nodes
        # instead, push the root onto a queue and calculate node indices via BFS
        '''
            0,1
            1,N    2,3
                3,4   4,5
              5,6  6,7
        '''
        while queue and index < len(nodes):
            node = queue.popleft()
            print(f"{index}: {node.val}")
            str_left = nodes[index]
            if str_left != "None":
                node_left = TreeNode(int(str_left))
                node.left = node_left
                queue.append(node_left)
            index += 1
            if index >= len(nodes):
                break
            str_right = nodes[index]
            if str_right != "None":
                node_right = TreeNode(int(str_right))
                node.right = node_right
                queue.append(node_right)
            index += 1
        return root



