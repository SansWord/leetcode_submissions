class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # parse expression
        operands, operators = self.parseExpr(expression)

        # genearte binary trees with multiple nodes
        exprTrees = self.generateBinaryTrees(len(operators))

        result = []
        for tree in exprTrees:
            val = self.evalTree(tree, deque(operands), deque(operators))
            result.append(val)


        # eval values for each binary tree
        return result
    
    # return [[operands], [operators]]
    def parseExpr(self, expression: str) -> tuple[deque[int], deque[str]]:
        operands = deque()
        operators = deque()

        digits = ""

        for c in expression:
            if c in "+-*":
                operands.append(int(digits))
                operators.append(c)
                digits = ""
            else:
                digits += c
        operands.append(int(digits))

        return operands, operators

    def evalTree(self, exprTree:TreeNode, operands:deque(int), operators:deque(int))->int:
        if exprTree is None:
            return operands.popleft()
        
        leftVal = self.evalTree(exprTree.left, operands, operators)
        curOperator = operators.popleft()
        rightVal = self.evalTree(exprTree.right, operands, operators)

        match curOperator:
            case "+":
                return leftVal + rightVal
            case "-":
                return leftVal - rightVal
            case "*":
                return leftVal * rightVal

        return 0

    @cache
    def generateBinaryTrees(self, n:int) -> list[TreeNode]:
        if n == 0:
            return [None]
        if n == 1:
            return [TreeNode(val=1)]
        
        result = []
        for i in range(n):
            leftTrees = self.generateBinaryTrees(i)
            rightTrees = self.generateBinaryTrees(n-i-1)
            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    result.append(TreeNode(val=1, left=leftTree, right=rightTree))


        return result
        
