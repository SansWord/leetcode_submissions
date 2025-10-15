class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        pre = float("-inf")
        for num in nums:
            if num != pre + 1:
                ranges.append([num, num])
            else:
                ranges[-1][1] = num
            pre = num
        
        res = []
        for start, end in ranges:
            if start != end:
                res.append(f"{start}->{end}")
            else:
                res.append(f"{start}")
        
        return res
        

        
