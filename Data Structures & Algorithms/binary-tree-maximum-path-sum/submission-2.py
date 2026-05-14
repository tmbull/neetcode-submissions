# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # approach
        # 1. compute result at each node - this would be the case where
        # the path passes through both children
        # 2. pass "single path" max up to parent
        # max path sum  = max(left, right, 0) + curr
        
        result = float('-inf')
        def dfs(node):
            nonlocal result
            if not node:
                return 0
            curr = node.val

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            result = max(result, curr + left + right)
            return curr + max(left, right)

        dfs(root)
        return result