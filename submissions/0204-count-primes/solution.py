class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        markers = [True] * (n)
        markers[0] = False
        markers[1] = False

        for i in range(2, int(math.sqrt(n))+1, 1):
            for j in range(i*i, n, i):
                if markers[j]:
                    markers[j] = False
        
        return len([t for t in markers if t])
        

        
