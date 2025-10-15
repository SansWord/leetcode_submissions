class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        minNum = float("inf")
        maxNum = float("-inf")
        numCounts = defaultdict(int)
        for i, num in enumerate(nums):
            numCounts[num] += 1
            minNum = num if num < minNum else minNum
            maxNum = num if num > maxNum else minNum
        
        vals = sorted(list(numCounts.keys()))

        maxLen = 0
        for val in vals:
            if val+1 in numCounts:
                currLen = numCounts[val] + numCounts[val+1]
                maxLen = maxLen if maxLen > currLen else currLen
            
        return maxLen
