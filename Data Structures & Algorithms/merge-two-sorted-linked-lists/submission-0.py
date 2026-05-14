# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        iter1 = list1
        iter2 = list2

        while iter1 and iter2:
            if iter1.val < iter2.val:
                current.next = iter1
                current = current.next
                iter1 = iter1.next
            else:
                current.next = iter2
                current = current.next
                iter2 = iter2.next
        
        while iter1:
            current.next = iter1
            current = current.next
            iter1 = iter1.next
        
        while iter2:
            current.next = iter2
            current = current.next
            iter2 = iter2.next

        return head.next
        



