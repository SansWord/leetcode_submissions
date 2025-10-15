class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        l = 0
        pre = float("-inf")
        incLens = []
        for r in range(len(nums)):
            num = nums[r]
            if num <= pre:
                incLens.append(r-l)
                l = r
            pre = num
        incLens.append(r-l+1)
        
        maxLen = 0
        pre = 0
        for l in incLens:
            halfLen = l // 2
            preLen = min(pre, l)

            maxLen = max(maxLen, halfLen, preLen)
            pre = l

        return maxLen


        
