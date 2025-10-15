class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        LEN = len(s)
        res = set()
        seen = set()
        for i in range(0, LEN-10+1):
            substr = s[i:i+10]
            if substr in seen:
                res.add(substr)
            else:
                seen.add(substr)
        
        return list(res)
