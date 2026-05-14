# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseRecursive(head)

    def reverseIter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        current = head

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        return prev

    def reverseRecursive(self, head: Optional[ListNode]):
        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.reverseRecursive(head.next)
            head.next.next = head
        head.next = None
        return new_head


