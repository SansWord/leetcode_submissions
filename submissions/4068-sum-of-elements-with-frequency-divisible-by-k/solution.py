class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        fq = defaultdict(int)
        for n in nums:
            fq[n] += 1
        
        res = 0
        for v, feq in fq.items():
            if feq % k == 0:
                res += v * feq

        return res
        
