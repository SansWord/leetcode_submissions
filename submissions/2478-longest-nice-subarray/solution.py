class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        maxLen = 0

        # bit mask
        curr = 0
        l = 0
        for r in range(LEN):
            num = nums[r]

            # check, shrink until it's a good window
            while curr & num:
                curr ^= nums[l]
                l += 1
            
            # it's a valid window, check max
            maxLen = max(maxLen, r - l +1)

            # add curr into bit mask
            curr |= num
        
        return maxLen
                
