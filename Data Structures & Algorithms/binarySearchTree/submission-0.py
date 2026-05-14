class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        new = Node(key, val)
        if not self.root:
            self.root = new
            return

        node = self.root
        while True:
            if node.key == key:
                node.val = val
                return
            elif key < node.key:
                if not node.left:
                    node.left = new
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = new
                    return
                node = node.right

    def get(self, key: int) -> int:
        def getNode(node, key):
            if node is None:
                return -1
            elif node.key == key:
                return node.val
            elif key < node.key:
                return getNode(node.left, key)
            else:
                return getNode(node.right, key)

        return getNode(self.root, key)


    def getMin(self) -> int:
        result = self.getMinNode(self.root)
        if result:
            return result.val
        else:
            return -1

    def getMinNode(self, curr) -> Node:
        while curr and curr.left:
            curr = curr.left
        return curr

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right

        if curr:
            return curr.val
        else: 
            return -1


    def remove(self, key: int) -> None:
        def removeNode(node, key) -> Node:
            if not node:
                return None
            if key < node.key:
                node.left = removeNode(node.left, key)
            elif key > node.key:
                node.right = removeNode(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    minRight = self.getMinNode(node.right)
                    node.key = minRight.key
                    node.val = minRight.val
                    node.right = removeNode(node.right, minRight.key)
            return node
        self.root = removeNode(self.root, key)

    def getInorderKeys(self) -> List[int]:
        def inOrderNode(node) -> List[int]:
            if not node:
                return []
            results = inOrderNode(node.left)
            results.append(node.key)
            results.extend(inOrderNode(node.right))

            return results
        return inOrderNode(self.root)

