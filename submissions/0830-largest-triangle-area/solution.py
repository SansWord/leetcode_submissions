class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def getArea(pointA, pointB, pointC) -> float:
            x1, y1 = pointA
            x2, y2 = pointB
            x3, y3 = pointC

            return 0.5 * abs((x1-x2)*(y1 - y3)-(x1-x3)*(y1-y2))
        
        point_count = len(points)
        result = 0
        for i in range(point_count-2):
            for j in range(i+1, point_count - 1):
                for k in range(j+1, point_count):
                    curr_area = getArea(points[i], points[j], points[k])
                    if result < curr_area:
                        result = curr_area

        return result
        
