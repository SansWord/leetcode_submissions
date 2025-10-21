class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        ans = [-1] * (LEN * 2)
        for i in range(LEN):
            ans[i] = ans[i+LEN] = nums[i]

        return ans
