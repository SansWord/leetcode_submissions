class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start and then by end. 
        intervals.sort()

        preStart, preEnd = intervals[0]
        res = []
        for interval in intervals[1:]:
            start, end = interval
            if preEnd < start:
                res.append([preStart, preEnd])
                preStart = start
                preEnd = end
            else:
                preEnd = max(preEnd, end)
        
        res.append([preStart, preEnd])
        return res
        
