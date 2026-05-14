# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # idea here is to get the "right-most value at each level" and add it to the results
        results = []
        q = deque()
        if root:
            q.append(root)

        while q:
            tmp = []
            for i in range(len(q)):
                curr = q.popleft()
                tmp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            results.append(tmp[-1])
        
        return results

