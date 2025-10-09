class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        previous = None
        preCount = 0
        curr = None
        currCount = 0

        for c in s:
            if c == curr:
                currCount += 1

            if c != curr:
                previous = curr
                preCount = currCount
                currCount = 1
                curr = c
            
            if currCount <= preCount:
                result+=1

        return result
        
