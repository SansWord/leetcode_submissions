class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occurrence = {}
        for i, n in enumerate(nums):
            if n not in occurrence:
                occurrence[n] = i
            else:
                if i - occurrence[n] <= k:
                    return True
                else:
                    occurrence[n] = i
        return False


