class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        res = [ [0] * n for _ in range(m) ]

        def avg(r, c) -> int:
            count = 0
            total = 0
            for i in [r-1, r, r+1]:
                for j in [c-1, c, c+1]:
                    if i >= 0 and i < m and j >=0 and j < n:
                        count += 1
                        total += img[i][j]
            return floor(total/count)


        for i in range(m):
            for j in range(n):
                res[i][j] = avg(i, j)
        

        
        return res
        
