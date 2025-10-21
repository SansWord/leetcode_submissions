class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # notice the tricky behavior of ceil and floor for python
        def div(a: int, b: int) -> int:
            if a/b < 0:
                return ceil(a/b)
            else:
                return floor(a/b)

        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": div
        }

        if len(tokens) == 1:
            return int(tokens[0])

        operandStack = []
        for token in tokens:
            if token not in operators:
                operandStack.append(int(token))
            else:
                operator = token
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                operandStack.append(operators[operator](operand1, operand2))

        return operandStack[0]

