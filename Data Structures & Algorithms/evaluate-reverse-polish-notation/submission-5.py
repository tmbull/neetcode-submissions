class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # process:
            # create a stack
            # read a token
                # if integer, push it onto stack
                # if operand
                    # pop two integers off the stack, and apply operand
                    # push result back onto the stack
            # result is on the top of the stack
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                x = stack.pop()
                y = stack.pop()
                result = 0
                match token:
                    case '+':
                        result = x + y
                    case '-':
                        result = y - x
                    case '*':
                        result = x * y
                    case _:
                        result = int(float(y) / x)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]
