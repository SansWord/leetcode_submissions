class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]

        lo = 0
        hi = len(nums)
        firstIdx = -1

        while lo < hi:
            mid = (lo + hi) // 2
            val = nums[mid]
            if val >= target:
                hi = mid
                if val == target:
                    firstIdx = mid
            else:
                lo = mid + 1
        
        lo = firstIdx
        hi = len(nums)
        lastIdx = -1

        while lo < hi:
            mid = (lo + hi) // 2
            val = nums[mid]


            if val <= target:
                lo = mid + 1
                if val == target:
                    lastIdx = mid
            else:
                hi = mid


        
        return [firstIdx, lastIdx]
        
