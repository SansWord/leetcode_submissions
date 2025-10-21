class Solution:
    def maxArea(self, height: List[int]) -> int:

        lIdx = 0
        rIdx = len(height) - 1
        maxArea = 0

        while lIdx < rIdx:
            lH = height[lIdx]
            rH = height[rIdx]
            area = min(lH, rH) * (rIdx - lIdx)
            maxArea = max(maxArea, area)

            if lH < rH:
                lIdx += 1
            else:
                rIdx -= 1

        return maxArea
        
