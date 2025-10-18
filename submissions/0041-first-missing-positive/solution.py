class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        LEN = len(nums)
        i = 0
        while i < LEN:
            num = nums[i]
            if 1 <= num and num <= LEN:
                idx = num - 1
                if nums[idx] != num:
                    # this means we swapp a new number to the current position
                    # should not proceed i
                    nums[i], nums[idx] = nums[idx], num
                    continue
            i += 1
        for i in range(LEN):
            if nums[i] != i+1:
                return i+1
        return LEN + 1

        
