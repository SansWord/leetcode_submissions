class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        LEN = len(words)

        result = []

        preWord = ""
        for word in words:
            if not self.areAnagrams(preWord, word):
                result.append(word)
                preWord = word

        return result
    
    def areAnagrams(self, word1: str, word2:str) -> bool:
        if len(word1) != len(word2):
            return False

        fq = defaultdict(int)
        for c in word1:
            fq[c] += 1
        
        for c in word2:
            if (not c in fq) or (fq[c] == 0):
                return False
            
            fq[c] -= 1
        return True

        
        
        
