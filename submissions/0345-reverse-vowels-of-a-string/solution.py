class Solution:
    def reverseVowels(self, s: str) -> str:
        LEN = len(s)
        if LEN == 0:
            return ""

        vowelIdxes = []
        vowels = "AEIOUaeiou"
        res = [ None for i in range(LEN) ]
        for i in range(LEN):
            c = s[i]
            if c in vowels:
                vowelIdxes.append(i)
            else:
                res[i] = c

        l = 0
        r = len(vowelIdxes) - 1
        while l <= r:
            res[vowelIdxes[l]] = s[vowelIdxes[r]]
            res[vowelIdxes[r]] = s[vowelIdxes[l]]

            l += 1
            r -= 1
        
        return "".join(res)
        
