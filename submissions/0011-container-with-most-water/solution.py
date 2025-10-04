class Solution:
    def maxArea(self, height: List[int]) -> int:

        lIdx = 0
        rIdx = len(height) - 1
        lH = height[lIdx]
        rH = height[rIdx]
        maxArea = min(lH, rH) * (rIdx - lIdx)

        while lIdx < rIdx:
            if lH < rH:
                lIdx += 1
                lH = height[lIdx]
            else:
                rIdx -= 1
                rH = height[rIdx]
            
            maxArea = max(maxArea, min(lH, rH) * (rIdx - lIdx))

        return maxArea
        
