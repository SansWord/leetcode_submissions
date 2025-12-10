class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        
        counts = {}

        pre = None
        curr = 0
        curr_count = 0

        for num in sorted_nums:
            if num != pre:
                curr += curr_count
                counts[num] = curr
                curr_count = 1
            else:
                curr_count += 1
            pre = num

        return [counts[n] for n in nums]
        
