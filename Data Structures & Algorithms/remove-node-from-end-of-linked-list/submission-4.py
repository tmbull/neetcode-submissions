# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # how to iterate to the end and back up
        # without using a stack
        # option 1: iterate twice:
        # once ot calculate length, again to find the -n element
        len = 0
        curr = head
        while curr:
            curr = curr.next
            len += 1
        
        count = len - n - 1
        if count < 0:
            return head.next

        curr = head
        while curr and count > 0:
            curr = curr.next
            count -= 1

        if curr.next:
            curr.next = curr.next.next


        return head