class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        fq = {chr(97+i):0 for i in range(26)}

        for c in magazine:
            fq[c] += 1

        for c in ransomNote:
            if fq[c] == 0:
                return False
            else:
                fq[c] -= 1
        
        return True
        
