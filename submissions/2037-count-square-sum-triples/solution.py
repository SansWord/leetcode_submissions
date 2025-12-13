class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                curr_sum = i**2 + j**2
                k = sqrt(curr_sum) // 1
                if k > n:
                    break
                elif k**2 == curr_sum and k <= n:
                    res += 1
        return res
        
