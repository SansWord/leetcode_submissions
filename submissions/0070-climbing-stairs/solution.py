class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = {
            0: 1,
            1: 1
        }
        
        return self.climb(n)

    def climb(self, n: int) -> int:
        if n <= 1:
            return 1
        if n in self.cache:
            return self.cache[n]

        n_1 = self.cache[n-1] if (n-1) in self.cache else self.climb(n-1)
        n_2 = self.cache[n-2] if (n-2) in self.cache else self.climb(n-2)
        
        result = n_1 + n_2
        self.cache[n] = result

        return result
        
