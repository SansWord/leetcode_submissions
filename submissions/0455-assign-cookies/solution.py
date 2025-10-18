class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        sLen = len(s)

        if sLen == 0:
            return 0

        count = 0
        sIdx = 0
        for greed in g:    
            while sIdx < sLen and greed > s[sIdx]:
                sIdx += 1
            
            if sIdx < sLen:
                count += 1
                sIdx += 1
            else:
                break
        
        return count

            
            
        
