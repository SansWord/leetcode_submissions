class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi)//2
            val = nums[mid]

            if val == target:
                return mid
            
            lVal = nums[lo]
            rVal = nums[hi - 1]

            if lVal < val:
                if target > val or target < lVal:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                if target < val or lVal <= target:
                    hi = mid
                else:
                    lo = mid + 1

        return -1
