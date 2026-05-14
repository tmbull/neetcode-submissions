# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good nodes - all ancestors are less than the current node
        # base cases - root is always good
        # must visit all nodes to count, so O(n) is best case
        # approach: dfs tracking max, 
        # at each node, increment if greater than max
        if not root:
            return 0
        
        count = 0
        
        def dfs(high, curr):
            nonlocal count
            if not curr:
                return

            if curr.val >= high:
                count += 1

            dfs(max(high, curr.val), curr.left)
            dfs(max(high, curr.val), curr.right)


        dfs(float('-inf'), root)
        return count