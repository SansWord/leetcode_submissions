class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        return self.pow(x, n)

    def pow(self, x:float, n:int) -> float :
        if n == 0:
            return 1
        if n == 1:
            return x

        if n < 0:
            return self.myPow(1/x, -n)

        bits = []
    
        while n != 0:
            bits.append(n%2)
            n //= 2

        result = 1
        while len(bits) != 0:
            result **= 2
            if bits.pop() == 1:
                result *= x
        
        return result
