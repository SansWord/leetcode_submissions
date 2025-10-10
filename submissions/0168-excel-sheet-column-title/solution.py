class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        result = []

        while columnNumber > 0:
            # why do we need -= 1 here?
            columnNumber -= 1
            result.append(chars[columnNumber%26])
            columnNumber //= 26

        return "".join(result[::-1])
        
