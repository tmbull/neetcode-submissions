class LRUCache:
    # We need two datastructures
    # 1. dict for cache O(1) lookup
    # 2. XXX for storing LRU object so that we can remove it from the cache if needed
    # 3. both GET and PUT should update usage
    # How to store usage? 
        # heap - O(logn) insertion, O(1) lookup for least recently used
        # linked list - O(1) insertion for append O(1) lookup if we link the element in the dict as well

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # head and tail are "dummy" nodes that juist contain pointers to the actual head/tail nodes
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self.delete(node)
        self.insert(key, node.val[1])
        # node values are (k,v) pairs
        return node.val[1]

        

    def put(self, key: int, value: int) -> None:
        # cache.size <= capacity and  item doesn't exist, just insert it
        # cache.size <= capacity and item does exist, just update it (and move to end of LRU list)
        # else if item exists, update value and move to end of LRU list
        # else item doesn't exist, evict LRU item and append current item to end of LRU list
        if key in self.cache:
            self.delete(self.cache[key])

        if len(self.cache) >= self.capacity:
            self.evictLRU()

        self.insert(key, value)

    def insert(self, key, value):
        node = Node((key,value))
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.cache[key] = node

    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        del(self.cache[node.val[0]])


    def evictLRU(self):
        # need to store KV in node so that we can also evict from cache
        self.delete(self.head.next)

    def moveToEnd(self, node):
        # set node.prev.next to node.next
        # set node.next.prev to node.prev
        # set node.prev to self.tail
        # set node.next to None
        # set self.tail to node
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = self.tail
        node.next = None
        self.tail = node
        
  

class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
