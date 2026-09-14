# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        iterate through nodes
        if node where node.val == val:
            set prev.next = curr.next
            set curr = curr.next
        else:
            set curr = curr.next
            set prev = curr
        '''
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next