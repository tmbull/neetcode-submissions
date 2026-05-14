class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        i = 0
        ptr = self.head
        while ptr and i < index:
            ptr = ptr.next
            i += 1
        if i < index or not ptr:
            return -1
        else:
            return ptr.val

    def insertHead(self, val: int) -> None:
        new_head = Node(val, self.head)
        self.head = new_head

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, None)
            return
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = Node(val, None)

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        i = 1
        ptr = self.head
        while ptr.next and i < index:
            ptr = ptr.next
            i += 1

        if i < index or not ptr.next:
            return False
        else:
            ptr.next = ptr.next.next
            return True

    def getValues(self) -> List[int]:
        result = []
        ptr = self.head
        while ptr:
            result.append(ptr.val)
            ptr = ptr.next
        return result
        
