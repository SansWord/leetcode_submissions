class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        LEN = len(nums)
        l = 0
        currAvg = sum(nums[:k])/k
        maxAvg = currAvg

        for r in range(k, LEN):
            newNum = nums[r]
            oldNum = nums[l]
            currAvg = currAvg + (newNum - oldNum)/k
            l+=1
            if currAvg > maxAvg:
                maxAvg = currAvg
        
        return maxAvg
        
