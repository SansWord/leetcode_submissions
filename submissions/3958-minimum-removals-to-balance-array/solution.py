class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        def findRight(nums, nk, start, end) -> int:
            #start: True
            #end: False
            while end - start > 1:
                mid = (end + start) // 2
                if nums[mid] <= nk:
                    start = mid
                else:
                    end = mid
            return start

        LEN = len(nums)
        if LEN == 1:
            return 0
        
        # O(NlogN)
        nums.sort()

        left = 0
        right = 0
        max_length = 0

        for left in range(LEN):
            nk = nums[left] * k
            right = findRight(nums, nk, right, LEN)
            curr_length = right - left + 1
            if max_length <= curr_length:
                max_length = curr_length
            
            # reaches right most, no need to increase minimum anymore.
            if right == LEN - 1:
                break

        return LEN - max_length
        



        

        
