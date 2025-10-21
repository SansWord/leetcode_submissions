class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        feqs = defaultdict(int)
        for num in nums:
            feqs[num] += 1
        h = []
        for v, feq in feqs.items():
            heapq.heappush(h, (-feq, v))
        res = []
        for i in range(k):
            feq, v = heapq.heappop(h)
            res.append(v)
        
        return res
        
