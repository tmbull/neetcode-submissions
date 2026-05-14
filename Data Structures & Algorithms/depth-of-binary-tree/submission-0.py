# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_depth(root, 0)

    def max_depth(self, root: Optional[TreeNode], current_depth: int) -> int:
        if root is None:
            return current_depth
        return max(self.max_depth(root.left, current_depth + 1), self.max_depth(root.right, current_depth + 1))