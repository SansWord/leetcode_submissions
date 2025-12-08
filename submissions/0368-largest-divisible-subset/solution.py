class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [ [n] for n in nums ]
        res = []

        for i in range(len(nums)-1, -1, -1):
            curr = nums[i]
            tmp = []
            for j in range(i+1, len(nums)):
                if nums[j] % curr == 0:
                    if len(dp[j]) > len(tmp):
                        tmp = dp[j]
            dp[i] = [curr] + tmp
            if len(dp[i]) > len(res):
                res = dp[i]
        return res
        
        
