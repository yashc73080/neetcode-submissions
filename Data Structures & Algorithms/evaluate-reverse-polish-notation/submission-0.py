class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # make new stack and append to it for every number, pop for every operator
        # operate on last 2 values
        # insert back into stack for each result

        def sub_result(n1, n2, operator):
            if operator == '+':
                return n1 + n2
            elif operator == '-':
                return n2 - n1
            elif operator == '*':
                return n1 * n2
            elif operator == '/':
                return int(n2 / n1)

        stack = []
        for token in tokens:

            # token is a number
            if token.lstrip('-').isnumeric():
                stack.append(int(token))

            # token is an operator
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                value = sub_result(num1, num2, token)

                stack.append(value)
            
        return stack[0]
