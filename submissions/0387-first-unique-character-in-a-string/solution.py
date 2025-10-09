class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        shown = set()
        unique_chars = set()
        for i in range(len(s)):
            c = s[i]
            if c not in shown:
                shown.add(c)
                unique_chars.add(c)
            else:
                if c in unique_chars:
                    unique_chars.remove(c)

        if unique_chars:            
            for i in range(len(s)):
                c = s[i]
                if c in unique_chars:
                    return i
        return -1


        
