class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)
        minDist = float("inf")
        result = float("inf")

        LEN = len(nums)

        for first in range(LEN-2):
            second = first + 1
            third = LEN - 1
            while second < third:
                total = nums[first] + nums[second] + nums[third]
                if total == target:
                    return target
                else:
                    dist = abs(total - target)
                    if dist < minDist:
                        minDist = dist
                        result = total

                    if total < target:
                        second += 1
                    else:
                        third -= 1

        return result

