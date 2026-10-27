# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        '''
        edge cases:
            null node - return (0,0)
            leaf node - return (val, val)

        

        need to keep track of:
            current path: max(left) + current + max(right)
            current max (max(left, right) + current)

            at each node return max(pathleft, pathright, current path)) and current max
            -15
        10      20
    n     n 15      5
           -5  -6

        '''
        def _max_path_sum(node) -> (int, int):
            '''
            returns (max_path, max_segment)
            '''
            if not node:
                return (float('-inf'), 0)
            # if not node.left not node.right:
            #     return (val, val)
            
            left_max_path, left_max_segment = _max_path_sum(node.left)
            right_max_path, right_max_segment = _max_path_sum(node.right)

            current_path_segment = max(0, left_max_segment, right_max_segment) + node.val
            current_path = max(0, left_max_segment) + node.val + max(0, right_max_segment)
            current_max_path = max(left_max_path, current_path, right_max_path)
            return current_max_path, current_path_segment

        
        result, _ = _max_path_sum(root)
        return result