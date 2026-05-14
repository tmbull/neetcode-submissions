# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        # we're iterating from the end and front of the list and "zipping them together"
        # we could push all of the nodes onto a stack and then pop 1/2 of them off the stack
        # o(n/2) space and time
        # is there an o(1) space soln? 
        # 1. Iterate to the middle of the list - two pointer approach
        # 2. Reverse the last half of the list
        # 3. "Zip" together the first half with the reversed second half
        # How to handle uneven length lists?
        # The middle element  goes to the end
        # So the head of hte second half should be after the middle element

        # find middle of the list
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # split the list and start second half from slow.next
        middle = slow.next
        slow.next = None

        # reverse the second half
        # [4,5,6] head 6,5,4
        # next points to self, 
        curr = middle
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # zip middle and start
        first = head
        second = prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
