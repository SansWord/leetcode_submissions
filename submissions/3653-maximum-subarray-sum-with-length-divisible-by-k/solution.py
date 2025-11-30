class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = {
            0:0
        }
        
        curr_sum = 0
        res = float("-inf")
        for i, v in enumerate(nums):
            curr_sum += v
            remainder = (i + 1) % k
            if not remainder in prefix:
                prefix[remainder] = curr_sum
            else:
                curr_res = curr_sum - prefix[remainder]
                res = max(res, curr_res)
                if curr_sum < prefix[remainder]:
                    prefix[remainder] = curr_sum
        return res

