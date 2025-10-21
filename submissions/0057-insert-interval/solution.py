class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        LEN = len(intervals)

        if LEN == 0:
            return [newInterval]

        newStart, newEnd = newInterval
        # binary search to find newInteveral[0] and newInteveral[1]
        l = -1
        r = LEN
        while r - l > 1:
            mid = l + (r-l)//2
            start, end = intervals[mid]

            if start > newStart:
                r = mid
            else:
                # start <= newStart
                l = mid
        
        # intervals[mid][0] <= newStart
        nearbyNewStart = l

        l = -1
        r = LEN
        while r - l > 1:
            mid = l + (r-l)//2
            start, end = intervals[mid]

            if end < newEnd:
                l = mid
            else:
                r = mid
        
        nearbyNewEnd = r

        if nearbyNewStart > 0:
            preRes = intervals[:nearbyNewStart]
        else:
            preRes = []

        if nearbyNewEnd < LEN - 1:
            postRes = intervals[nearbyNewEnd + 1:]
        else:
            postRes = []

        midRes = []
        
        # handling nearbyNewEnd == LEN and nearbyNewStart == -1
        if nearbyNewStart != -1:
            startInterval = intervals[nearbyNewStart]
            if startInterval[1] < newStart:
                midRes.append(startInterval)
                start = newStart
            else:
                start = startInterval[0]
        else:
            start = newStart
        
        if nearbyNewEnd != LEN:
            endInterval = intervals[nearbyNewEnd]
            if endInterval[0] > newEnd:
                midRes.append([start, newEnd])
                midRes.append(endInterval)
            else:
                midRes.append([start, endInterval[1]])
        else:
            midRes.append([start, newEnd])

        return preRes + midRes + postRes



        
