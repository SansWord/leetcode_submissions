class Solution:
    def longestValidParentheses(self, s: str) -> int:
        LEN = len(s)
        maxLen = 0
        pStack = [-1]
        

        for idx, p in enumerate(s):
            if p == "(":
                pStack.append(idx)
            if p == ")":
                if len(pStack) == 1:
                    pStack[0] = idx
                else:
                    pStack.pop()
                    currLen = idx - pStack[-1]
                    maxLen = maxLen if maxLen >= currLen else currLen
        return maxLen
