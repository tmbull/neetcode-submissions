class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Need to use a stack
        # push operands onto the stack
        # pop when we encounter an operator
        # [1 2]
        # [3]
        # [3 3]
        # [9]
        # [9 4]
        # 5
        stack = []
        for token in tokens:
            if token == '+':
                y = stack.pop()
                x = stack.pop()
                stack.append(x + y)
            elif token == '-':
                y = stack.pop()
                x = stack.pop()
                stack.append(x - y)
            elif token == '*':
                y = stack.pop()
                x = stack.pop()
                stack.append(x * y)
            elif token == '/':
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x / y))
            else:
                stack.append(int(token))
        
        return stack.pop()
