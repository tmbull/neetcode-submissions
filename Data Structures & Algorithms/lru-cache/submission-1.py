class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.first = Node(0,0)
        self.last = Node(0,0)
        self.first.next = self.last
        self.last.prev = self.first
        self.capacity = capacity

    def lruRemove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def lruInsert(self, node):
        prev, next = self.last.prev, self.last
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.lruRemove(node)
            self.lruInsert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.lruRemove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.lruInsert(node)

        if len(self.cache) > self.capacity:
            node = self.first.next
            self.lruRemove(node)
            del self.cache[node.key]
        
