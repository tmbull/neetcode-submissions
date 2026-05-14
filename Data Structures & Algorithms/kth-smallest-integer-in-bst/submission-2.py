# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # count = 0
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     # we want to traverse in ascending order, so this is another in order DFS traversal
    #     if not root:
    #         return None
    #     result = self.kthSmallest(root.left, k)
    #     if result:
    #         return result
    #     self.count += 1
    #     if k == self.count:
    #         return root.val
    #     return self.kthSmallest(root.right, k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we want to traverse in ascending order, so this is another in order DFS traversal
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right