# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        current_max = 0
        def dfs(current) -> (int, int):
            if not current:
                return 0, 0

            max_left, left = dfs(current.left) 
            max_right, right = dfs(current.right)
            current_max = max(max_left, max_right)

            current_diameter = 1 + max(left, right)
            current_max = max(current_max, left + right)

            return current_max, current_diameter

        current_max, _ = dfs(root)

        return current_max