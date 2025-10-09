class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hayLength = len(haystack)
        needleLength = len(needle)

        for i, v in enumerate(haystack):
            if hayLength - i < needleLength:
                return -1

            if haystack[i:i+needleLength] == needle:
                return i
        
        return -1
