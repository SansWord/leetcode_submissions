class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def getVisitTime(source: List[int], dest: List[int]) -> int:
            x1, y1 = source
            x2, y2 = dest
            hori_dist = abs(x1 - x2)
            vert_dist = abs(y1 - y2)
            return min(hori_dist, vert_dist) + abs(hori_dist - vert_dist)
        
        if len(points) == 1:
            return 0
        total_time = 0
        for i in range(len(points) - 1):
            total_time += getVisitTime(points[i], points[i+1])
        return total_time

        
