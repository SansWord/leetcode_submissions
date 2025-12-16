class Solution:
    def maxSum(self, nums: List[int]) -> int:
        shown = set()
        maxNegative = float("-inf")
        result = 0
        for n in nums:
            if n > 0 and n not in shown:
                shown.add(n)
                result += n
            else:
                if maxNegative < n:
                    maxNegative = n


        return result if len(shown) != 0 else maxNegative

        
