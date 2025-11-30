class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        
        min_prefix = 0
        res = float("-inf")

        for num in nums:
            curr_sum += num
            curr_max = curr_sum - min_prefix
            res = max(res, curr_max)
            min_prefix = min(min_prefix, curr_sum)
        
        return res


