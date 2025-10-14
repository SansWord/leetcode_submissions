class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # evenCount = 5
        # primeCount = 4
        # every two digits has 20 choice
        # half = n // 2
        # 20**half * (5 if n is odd else 1)
        

        prime = 1000000007

        # for a given prime, x^(p-1) % p = 1
        # hence x^k = x^(k%(p-1))
        # we're calculating 20 && n//2, hence mod 2*(p-1)
        n = n % (2*(prime-1))

        hasOddDigits = n % 2 == 1
        half = n // 2

        bits = []
        while half > 0:
            bits.append(half%2)
            half//=2

        res = 1
        while len(bits):
            res = (res**2) % prime
            if bits.pop() == 1:
                res = res * 20 % prime

        if hasOddDigits:
            res = res * 5 % prime
        
        return res
        
        
