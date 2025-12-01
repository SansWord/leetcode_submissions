class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        LEN1 = len(num1)
        LEN2 = len(num2)

        result = [ 0 for _ in range(LEN1 + LEN2) ]

        d1_pos = 0
        d2_pos = 0
        for d1_pos in range(LEN1):
            for d2_pos in range(LEN2):
                d1 = int(num1[LEN1 - d1_pos - 1])
                d2 = int(num2[LEN2 - d2_pos - 1])

                mul = d1 * d2
                curr = result[d1_pos + d2_pos] + mul

                result[d1_pos + d2_pos] = curr % 10
                result[d1_pos + d2_pos + 1] += curr // 10


        # remove leading 0 (which is at the end of result)
        while result[-1] == 0:
            result.pop()
        
                
        return "".join(reversed([str(n) for n in result]))



        
        
        
