"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # basic approach - iterate through next pointers to build list
        # create a map of old -> new
        # iterate through random pointers to assign random pointers in new 
        if not head:
            return None

        dummy = Node(0)

        lookup = {}

        curr = head
        result_curr = dummy
        while curr:
            result_curr.next = Node(curr.val)
            result_curr = result_curr.next
            lookup[curr] = result_curr
            curr = curr.next


        curr = head
        while curr:
            if curr.random:
                lookup[curr].random = lookup[curr.random]
            curr = curr.next

        return dummy.next
            