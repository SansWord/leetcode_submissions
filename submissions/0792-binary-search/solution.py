class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            val = nums[mid]
            if val == target:
                return mid
            
            if target < val:
                hi = mid
            else:
                lo = mid + 1
        
        return -1
            
        
