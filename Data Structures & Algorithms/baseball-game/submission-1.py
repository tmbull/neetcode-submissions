class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # put numbers straight into the stack
        # if (+), peek at the previous 2 items on the stack and add them
        # if (C), pop the previous item off the stack
        # if (D), peek at the previous 1 item ont he stack, double it, and add the reuslt to the stack
        # at the end, sum the stack

        stack = []

        for op in operations:
            if op == "+": # and len(stack) > 1:
                res = stack[-1] + stack[-2]
                stack.append(res)
            elif op == "C": # and stack:
                stack.pop()
            elif op == "D": # and len(stack) > 0:
                res = stack[-1] * 2
                stack.append(res)
            else:
                stack.append(int(op))

        return sum(stack)
                
