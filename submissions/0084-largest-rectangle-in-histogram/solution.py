class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        LEN = len(heights)
        leftMost = [-1] * LEN
        rightMost = [LEN] * LEN

        stack = []
        for i, h in enumerate(heights):
            # pop until stack[-1] is lower than h, meaning it is bounded
            while stack and heights[stack[-1]] >= h:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(LEN-1, -1, -1):
            h = heights[i]
            # pop until stack[-1] is lower than h, meaning it is bounded
            while stack and heights[stack[-1]] >= h:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        maxArea = 0
        for i in range(LEN):
            h = heights[i]
            leftIdx = leftMost[i]
            rightIdx = rightMost[i]
            area = h * ((rightIdx - 1) - (leftIdx + 1) + 1)
            maxArea = max(maxArea, area)

        return maxArea

        
