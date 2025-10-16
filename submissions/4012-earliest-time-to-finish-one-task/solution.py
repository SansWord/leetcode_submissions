class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = float("inf")
        for st, t in tasks:

            time = st + t
            if res > time:
                res = time
        
        return res
        
