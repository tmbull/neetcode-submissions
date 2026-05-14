# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # approach:
            # iterate to the end of the list to get the count
            # iterate again to the len - n element
        dummy = ListNode(next=head)

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        target = length - n
        # ex. len 2, n = 2
        # len - 2 = 0
        # start from dummy, so we stop at the node before the one to remove
        curr = dummy
        i = 0
        while i < target:
            curr = curr.next
            i += 1

        if curr.next:
            curr.next = curr.next.next

        return dummy.next


