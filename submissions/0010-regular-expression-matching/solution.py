class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # construct pattern into a graph
        pattern = []
        for c in p:
            if c != "*":
                pattern.append([c,False])
            else:
                pattern[-1][1] = True
                
                if len(pattern) >= 2:
                    # remove redumdent pattern to avoid pattern attack:
                    # a*a* equal to a*
                    # .*a* equals to .*
                    # .*.* eqaul to .*
                    # a*.* equals to .*


                    if pattern[-2][1]:
                        if pattern[-1][0] == ".":
                            currP = pattern.pop()
                            pattern.pop() # remove previous pattern
                            pattern.append(currP)

                        elif pattern[-2][0] == "." or pattern[-2][0] == pattern[-1][0]:
                            pattern.pop()

        # walk through s with the graph.
        self.s = s
        self.sLen = len(s)
        self.pattern = pattern
        self.pLen = len(pattern)
        return self.matchPattern(0, 0)
        
    
    def matchPattern(self, sIdx: int, pIdx: int) -> bool:
        
        if pIdx == self.pLen: # pattern is fully consumed, check if s is fully consumed
            return sIdx == self.sLen

        if sIdx == self.sLen: # reach end of s, check if all left pattern are *
            for p in self.pattern[pIdx:]:
                if not p[1]:
                    # print("p fully consumed, False")
                    return False
            return True

        currC = self.s[sIdx]
        currP = self.pattern[pIdx]
        currPChr = currP[0]
        currPStar = currP[1]

        # print(currC, currP, sIdx, pIdx)
        if not currPStar:
            if currPChr != "." and currPChr != currC:
                # print("not match, False")
                return False
            else:
                return self.matchPattern(sIdx+1, pIdx+1)
        
        else: # pattern with *
            if currPChr == "." or currPChr == currC:
                # consume patter or not
                return (
                    self.matchPattern(sIdx+1, pIdx+1)  # consume s and pattern
                    or self.matchPattern(sIdx+1, pIdx) # consume s but keep pattern
                    or self.matchPattern(sIdx, pIdx+1) # consume pattern (* = 0)
                )
            else:
                # have to consume pattern
                return self.matchPattern(sIdx, pIdx+1)
