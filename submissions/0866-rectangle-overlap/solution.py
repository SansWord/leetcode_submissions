class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        def isOverlap(a1, a2, b1, b2) -> bool:
            return not (b1 >= a2 or b2 <= a1)

        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2

        return isOverlap(ax1, ax2, bx1, bx2) and isOverlap(ay1, ay2, by1, by2)
        
