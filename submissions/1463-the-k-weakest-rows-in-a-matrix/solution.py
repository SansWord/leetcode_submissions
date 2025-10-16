class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        q = []
        for i in range(len(mat)):
            row = mat[i]
            heapq.heappush(q, [sum(row), i])
        
        res = []
        for i in range(k):
            power, idx = heapq.heappop(q)
            res.append(idx)
        
        return res
