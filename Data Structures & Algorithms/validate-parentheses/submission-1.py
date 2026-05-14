class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(', '{', '['}
        matches = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            elif not stack:
                return False
            else:
                top = stack.pop()
                if c != matches[top]:
                    return False

        return not stack

        