class Solution:
    def numSub(self, s: str) -> int:
        MAX = 10**9 + 7
        result = 0
        
        curr = 0
        for i in s:
            if i == "0":
                curr = 0
            else:
                curr += 1
                result = (result + curr) % MAX

        return result

        
