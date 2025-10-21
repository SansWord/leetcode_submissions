class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = -1
        r = len(nums)-1

        while r - l > 1:
            mid = l + (r-l)//2

            # if l == -1, it would take the last element of the list and still maintain invariant
            lVal = nums[l]
            mVal = nums[mid]
            rVal = nums[r]

            if lVal < rVal:
                return lVal
            
            if lVal > rVal:
                if mVal >= lVal:
                    l = mid
                else:
                    r = mid
            else:
                # lVal == rVal
                if mVal > lVal:
                    l = mid
                elif mVal < lVal:
                    r = mid
                else:
                    # lVal == mVal == rVal
                    l += 1
        return nums[r]
        
