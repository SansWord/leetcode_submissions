class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = -1
        hi = len(nums)
        while hi - lo > 1:
            mid = (lo+hi)//2
            val = nums[mid]
            if target < val:
                hi = mid
            else:
                lo = mid

        # nums[lo] <= target
        # nums[hi] > target
        return -1 if lo == -1 or nums[lo] != target else lo

