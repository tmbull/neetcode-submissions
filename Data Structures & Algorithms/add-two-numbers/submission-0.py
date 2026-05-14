# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse order means we can do normal addition with carry
        return self.add(l1, l2, 0)

    def add(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        total = carry
        next_l1 = None
        next_l2 = None
        if not l1 and not l2:
            if carry:
                return ListNode(carry, None)
            else:
                return None
        if l1:
            total += l1.val
            next_l1 = l1.next
        if l2:
            total += l2.val
            next_l2 = l2.next
        digit = total % 10
        next_carry = total // 10
        return ListNode(digit, self.add(next_l1, next_l2, next_carry))
            
