class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        segs = []
        pre = float("-inf")
        for n in prices:
            if pre - n != 1:
                segs.append(1)
            else:
                segs[-1] += 1
            pre = n

        res = 0
        for n in segs:
            res += n
            res += n*(n-1) // 2

        return res

        
