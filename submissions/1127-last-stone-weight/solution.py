class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for s in stones:
            heapq.heappush(q, -s)
        while len(q) > 1:
            s1 = heapq.heappop(q)
            s2 = heapq.heappop(q)
            if s1 != s2:
                heapq.heappush(q, s1 - s2)
        return 0 if not q else -q[0]
        
