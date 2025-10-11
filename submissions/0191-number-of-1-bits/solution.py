class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n > 0:
            bits += n % 2
            n //= 2

        return bits
        
