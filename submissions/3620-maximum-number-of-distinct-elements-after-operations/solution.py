class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        fq = defaultdict(int)
        for num in nums:
            fq[num] += 1
        sorted_distinct_nums = sorted(list(fq.keys()))
        counts = 0
        upper = float("-inf")
        for num in sorted_distinct_nums:
            f = fq[num]
            lower = max(num - k, upper)
            upper = num + k
            
            if lower <= upper:
                count = min(upper - lower + 1, f)
                upper = lower + count
                counts += count

        return counts
