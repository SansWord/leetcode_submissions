class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        sorted_box = reversed(sorted(capacity))
        
        if total_apples == 0:
            return 0

        box_used = 0
        for c in sorted_box:
            box_used += 1
            if c >= total_apples:
                return box_used
            else:
                total_apples -= c
        
        
