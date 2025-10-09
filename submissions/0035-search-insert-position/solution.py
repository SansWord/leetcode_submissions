class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = len(nums)
        lo = 0
        hi = len(nums)

        # search idx of upper bound
        while lo < hi:
            mid = (lo+hi) // 2
            val = nums[mid]

            if val == target:
                return mid
            else:
                if val > target:
                    idx = mid
                    hi = mid
                else:
                    lo = mid + 1
        
        return idx
        
        
