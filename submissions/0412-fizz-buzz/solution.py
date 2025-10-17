class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(n):
            k = i + 1
            if k % 15 == 0:
                res.append("FizzBuzz")
            elif k % 3 == 0:
                res.append("Fizz")
            elif k % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(k))
        
        return res
