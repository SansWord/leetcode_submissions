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

            
            if lVal < rVal:
                # normal BFS
                if val < target:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                # in rotated segments
                if lVal <= target:
                    # target in first segment
                    if val < target:
                        # check if val in first or second segment
                        if val >= lVal:
                            # val in first segment, search right
                            lo = mid + 1
                        else:
                            # val in second segment, search left
                            hi = mid
                    else:
                        # search left
                        hi = mid
                else:
                    # target in second segment
                    if val < target:
                        # search right
                        lo = mid + 1
                    else:
                        # check if val in first or second segment
                        if val >= lVal:
                            # val in first segment, search right
                            lo = mid + 1
                        else:
                            # val in second segment, search left
                            hi = mid

        return -1
