class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        LEN = n + 1

        minK = 0
        maxK = n

        result = [-1] * LEN

        for i in range(n):
            c = s[i]
            if c == "I":
                result[i] = minK
                minK += 1
            else:
                result[i] = maxK
                maxK -= 1
        result[n] = minK
        return result
