class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def get_ans(n:int) -> int:
            if n == 2:
                return -1
            else:
                for i in range(n):
                    if i|i+1 == n:
                        return i

        ans = [ get_ans(n) for n in nums ]
        return ans
        
