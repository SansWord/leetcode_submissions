class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.mem = [None] * (n+1)
        return self.calculate(n)

    def calculate(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]

        if self.mem[n]:
            return self.mem[n]

        else:
            result = []
            
            # iterate over for the len of first parentheses
            # it could be from 1*2 to n*2
            # hence it looks like f"({preP}){postP}" for preP from 0*2 to (n-1)*2
            # and length of postP is n - 1 - preP

            for i in range(n-1, -1, -1):
                prePs = self.calculate(i)
                postPs = self.calculate(n-i-1)

                for preP in prePs:
                    for postP in postPs:
                        result.append(f"({preP}){postP}")

        return result
