class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        rainSum = 0
        lIdx = 0
        lMax = height[0]
        rIdx = len(height)-1
        rMax = height[rIdx]

        while lIdx < rIdx:
            if lMax < rMax:
                lIdx += 1
                h = height[lIdx]
                if lMax > h:
                    rainSum += lMax - h
                else:
                    lMax = h
            else:
                rIdx -= 1
                h = height[rIdx]
                if rMax > h:
                    rainSum += rMax - h
                else:
                    rMax = h

        return rainSum

