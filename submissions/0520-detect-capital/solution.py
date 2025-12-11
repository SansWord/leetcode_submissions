class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.lower() == word or word.upper() == word or word[0].lower() + word[1:] == word.lower()
        
