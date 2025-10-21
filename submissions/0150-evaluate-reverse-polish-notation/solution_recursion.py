class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            raise Exception("Should not happen")

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

        token = tokens.pop()
        if token not in operators:
            return int(token)
        else:
            operator = token
            operand2 = self.evalRPN(tokens)
            operand1 = self.evalRPN(tokens)

            return operators[operator](operand1, operand2)

