class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        preColor = None
        totalTime = 0

        localMax = 0

        for i in range(len(colors)):

            currColor = colors[i]
            currTime = neededTime[i]

            if currColor != preColor:
                preColor = currColor
                localMax = currTime
            else:
                if currTime > localMax:
                    totalTime += localMax
                    localMax = currTime
                else:
                    totalTime += currTime

        return totalTime
