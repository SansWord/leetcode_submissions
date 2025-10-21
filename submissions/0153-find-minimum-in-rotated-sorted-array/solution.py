class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = -1
        r = len(nums)-1

        while r - l > 1:
            mid = l + (r-l)//2
            
            # handle when l = -1
            lVal = nums[l]
            mVal = nums[mid]
            rVal = nums[r]


            if lVal < rVal:
                # normal segment, lVal is the smallest
                return lVal
            
            else:
                # rotated segment
                if lVal > mVal:
                    # mVal is in the second segment
                    r = mid
                else:
                    # mVal is in the first segment
                    l = mid
        
        return nums[r]

        
