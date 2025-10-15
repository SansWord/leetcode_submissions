class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        # first: calculate a set that can construct nice substring
        possibleC = set(s)
        
        impossibleC = set()
        for c in possibleC:
            flippedC = c.upper() if c.islower() else c.lower()
            if not flippedC in possibleC:
                impossibleC.add(c)
        
        # s consists of all possible c, meaning the whole string is nice
        if len(impossibleC) == 0:
            return s

        for c in impossibleC:
            possibleC.remove(c)

        # there's no possible c, meaning no substring is nice, return empty string
        if len(possibleC) == 0:
            return ""


        for i in range(len(s)):
            c = s[i]
            if c in impossibleC:
                # devide and conquer into left and right string.
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                # we want the earilest, hence using >= so if equal, take the left one
                return left if len(left) >= len(right) else right
                
        return ""

        
