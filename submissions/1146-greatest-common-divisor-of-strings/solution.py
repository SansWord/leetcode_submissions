class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        
        if len(str1) > len(str2):
            big = str1
            small = str2
        elif len(str1) < len(str2):
            big = str2
            small = str1
        else: # equal but not the same, they don't have gcd
            return ""

        while big != small:
            smallLen = len(small)
            while big.startswith(small):
                big = big[smallLen:]
            
            if len(big) == 0:
                return small
            if len(big) >= smallLen:
                return ""
            
            big, small = small, big

        return ""

        
