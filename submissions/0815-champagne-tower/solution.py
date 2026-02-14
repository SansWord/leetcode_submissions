class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        parent = [poured]

        for i in range(1,query_row+1):
            child = [0] * (i+1)
            for j in range(i):
                if parent[j] > 1:
                    extra = (parent[j] - 1) / 2
                    child[j] += extra
                    child[j+1] += extra
            parent = child

        return min(parent[query_glass], 1)
        
