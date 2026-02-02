class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        result = len(words)
        for word in words:
            for c in brokenLetters:
                if c in word:
                    result -= 1
                    break
        
        return result
        
