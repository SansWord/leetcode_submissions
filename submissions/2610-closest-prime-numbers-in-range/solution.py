class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        
        marks = [True] * (right + 1)
        marks[0] = False
        marks[1] = False

        for i in range(2, math.ceil(math.sqrt(right)) + 1):
            for j in range(i*i, right+1, i):
                marks[j] = False
        # marks is now properly processed, p is prime if marks[p]


        p = -1
        m = float('inf')
        r = [-1, -1]
        for i in range(left, right + 1):
            if marks[i]:
                if p != -1 and i - p < m:
                    m = i - p
                    r = [p, i]
                p = i

        return r

