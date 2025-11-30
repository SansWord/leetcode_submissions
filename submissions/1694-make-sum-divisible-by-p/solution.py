class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        LEN = len(nums)
        remainder = sum(nums) % p
        if remainder == 0:
            return 0

        # find remainder
        result = LEN
        curr_sum = 0
        remain_to_idx = {
            0: -1
        }
        for i, v in enumerate(nums):
            curr_sum = (curr_sum + v) % p
            removing_prefix_sum = (curr_sum - remainder + p) % p
            if removing_prefix_sum in remain_to_idx:
                sub_arr_len = i - remain_to_idx[removing_prefix_sum]
                result = min(result, sub_arr_len)
            remain_to_idx[curr_sum] = i
    
        if result != float("inf") and result != LEN:
            return result
        else:
            return -1
        
