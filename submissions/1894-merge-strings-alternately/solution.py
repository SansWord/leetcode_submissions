class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1Length = len(word1)
        w2Length = len(word2)
        result = ""

        for i in range(min(w1Length, w2Length)):
            result += word1[i]
            result += word2[i]

        if w1Length > w2Length:
            result += word1[w2Length:]
        elif w2Length > w1Length:
            result += word2[w1Length:]

        return result
        
