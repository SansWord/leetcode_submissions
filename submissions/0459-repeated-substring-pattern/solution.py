class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        LEN = len(s)
        rotated = s * 2
        for subLen in range(1, LEN//2 + 1):
            if LEN % subLen == 0:
                if rotated[subLen:subLen+LEN] == s:
                    return True
        
        return False

        
