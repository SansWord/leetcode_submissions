class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1

        pre = 0
        result = 1        
        while n >= 2:
            pre, result = result, result + pre
            n -= 1
        
        return result

        
