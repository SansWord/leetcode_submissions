class Solution:
    def scoreBalance(self, s: str) -> bool:
        # ord('a') is 97
        scores = [
            ord(c) - 96 for c in s
        ]

        LEN = len(scores)

        leftSums = [-1] * LEN
        rightSums = [-1] * LEN

        leftSums[0] = scores[0]
        rightSums[-1] = 0

        # leftSums is inclusive
        for i in range(1, LEN):
            leftSums[i] = leftSums[i-1] + scores[i]
        
        # rightSums is exclusive
        for i in range(LEN-2,-1,-1):
            rightSums[i] = rightSums[i+1] + scores[i+1]
        
        for i in range(LEN):
            if leftSums[i] == rightSums[i]:
                return True
        
        return False
        
