class Solution:
    def longestPalindrome(self, s: str) -> int:
        fq = defaultdict(int)
        for c in s:
            fq[c] += 1
        
        res = 0
        hasOdd = False
        for c, f in fq.items():
            if f % 2 == 0:
                res += f
            else:
                hasOdd = True
                res += (f-1)


        if hasOdd:
            res += 1
        return res
