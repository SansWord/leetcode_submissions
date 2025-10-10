class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = [ c.lower() for c in s if c.isalnum() ]

        l = 0
        r = len(chars) - 1

        while l < r:
            lC = chars[l]
            rC = chars[r]
            if lC != rC:
                return False
            l += 1
            r -= 1

        return True
        
