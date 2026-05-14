# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # option 1: divide and conquer
            # merge the lists 2 at a time until they're all merged together
        # option 2:
            # sort them all at once... will this work?
            # iterate through current index and take the min
            # O(n*k)
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged.append(self.mergeLists(l1, l2))
            lists = merged
        return lists[0]


    def mergeLists(self, l1, l2) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return head.next

    