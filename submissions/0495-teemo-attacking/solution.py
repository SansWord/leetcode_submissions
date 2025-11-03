class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        pre = timeSeries[0]
        for t in timeSeries[1:]:
            if t - pre >= duration:
                total += duration
            else:
                total += t - pre
            pre = t
        
        total += duration

        return total
        
