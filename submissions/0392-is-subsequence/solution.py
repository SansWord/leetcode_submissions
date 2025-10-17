class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if t == "":
            return False
        
        curSIdx = 0
        curSChr = s[curSIdx]
        sLen = len(s)
        for c in t:
            if c == curSChr:
                curSIdx += 1
                if curSIdx == sLen:
                    return True
                curSChr = s[curSIdx]
        
        return False

        
