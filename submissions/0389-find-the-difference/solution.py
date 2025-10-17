class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        fq = {chr(97 + i): 0 for i in range(26)}
        for c in s:
            fq[c] += 1
        
        for c in t:
            if fq[c] == 0:
                return c
            else:
                fq[c] -= 1
        
