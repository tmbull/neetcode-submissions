class MyHashMap:
    # Memory-efficient solution - use a dynamic array, hash function, and modulus to calculate indices
    def __init__(self):
        # need to init to a specific size
        self.table = [ListNode(-1, -1) for _ in range(1_000)];
        

    def put(self, key: int, value: int) -> None:
        bucket = key % 1000;
        head = self.table[bucket];
        while head.next:
            if head.next.key == key:
                head.next.val = value;
                return;
            head = head.next;
        
        head.next = ListNode(key, value);


    def get(self, key: int) -> int:
        bucket = key % 1000;
        head = self.table[bucket].next;
        while head:
            if head.key == key:
                return head.val;
            head = head.next;

        return -1;

    def remove(self, key: int) -> None:
        bucket = key % 1000;
        head = self.table[bucket];
        while head.next:
            if head.next.key == key:
                head.next = head.next.next;
                return;
            head = head.next;

        
class ListNode:
    def __init__(self, key, val):
        self.key = key;
        self.val = val;
        self.next = None;


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)