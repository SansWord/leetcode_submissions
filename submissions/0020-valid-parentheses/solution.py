class Solution:
    def isValid(self, s: str) -> bool:
        matched_brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        open_brackets = []

        for c in s:
            if c in "([{":
                open_brackets.append(c)
            else:
                if len(open_brackets) == 0 or matched_brackets[c] != open_brackets[-1]:
                    return False
                else:
                    open_brackets.pop()

        return len(open_brackets) == 0

        
