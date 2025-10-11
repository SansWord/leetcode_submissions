class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        lettersToIterate = []
        for d in digits:
            lettersToIterate.append(letters[d])

        return self.generateCombination(lettersToIterate, 0)
    
    def generateCombination(self, lettersToIterate: list[str], idx: int) -> list[str]:
        if len(lettersToIterate) - 1 == idx:
            return [ c for c in lettersToIterate[idx] ]
        
        result = []

        for com in self.generateCombination(lettersToIterate, idx + 1):
            for c in lettersToIterate[idx]:
                result.append(c+com)
        
        return result
