class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums)
        result = 0
        for i in range(N):
            evens = set()
            odds = set()
            for j in range(i, N):
                # check if array is balance and keep the largest
                curr = nums[j]
                if curr % 2 == 0:
                    evens.add(curr)
                else:
                    odds.add(curr)
                
                if len(evens) == len(odds):
                    # balance array from i to j
                    result = max(result, j - i + 1)
        
        return result

