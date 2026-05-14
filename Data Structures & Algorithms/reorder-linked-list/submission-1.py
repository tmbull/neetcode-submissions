# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        # we want to re-order the second half of the list and interleave with
        # the first half of the list
        # easiest way to do this is to reverse the second half
        # then iterate the first and second ahlf at the same time and zip them together
        # Find midpoint
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # interleave lists
        dummy = ListNode()
        curr = dummy
        odd = head
        even = prev
        print(f"{odd}")
        print(str(even))
        while even:
            curr.next = odd
            odd = odd.next
            curr.next.next = even
            even = even.next
            curr = curr.next.next
        if odd:
            curr.next = odd

        head = dummy.next





            



        
