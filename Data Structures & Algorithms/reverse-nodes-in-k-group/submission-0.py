# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # # iterate until the kth node
        # # reverse all nodes prior
        # # continue iteration again

        # curr = head
        # i = 1
        # while i < k and curr.next:
        #     curr = curr.next # 1, 2 # 2, 3
        #     i += 1 # 2 # 3

        # prev = curr
        # curr = curr.next
        # # next is the head of the next group
        # next = curr.next

        # # reverse list

        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            i = 0
            kth = group_prev
            while kth and i < k:
                kth = kth.next
                i += 1
            if not kth:
                break
            group_next = kth.next
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

            # curr_str = curr.val if curr else 'None'
            # next_str = next.val if next else 'None'

            # print(f"{prev.val}, {curr_str}, {next_str}")
        return dummy.next