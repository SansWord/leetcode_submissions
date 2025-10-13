class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.stack = []
        self.n = n
        self.calculate(0, 0)
        return self.result

    def calculate(self, openP: int, closeP: int) -> None:
        if openP == closeP and openP == self.n:
            self.result.append("".join(self.stack))
            return
        
        if openP < self.n:
            self.stack.append("(")
            self.calculate(openP+1, closeP)
            self.stack.pop()
        
        if openP > closeP:
            self.stack.append(")")
            self.calculate(openP, closeP+1)
            self.stack.pop()
