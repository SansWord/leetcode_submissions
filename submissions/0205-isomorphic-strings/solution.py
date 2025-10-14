class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mappedC = set()
        for i in range(len(s)):
            cS = s[i]
            cT = t[i]

            if cS not in mapping:
                if cT in mappedC:
                    return False
                mapping[cS] = cT
                mappedC.add(cT)
            else:
                if cT != mapping[cS]:
                    return False
        return True
        
