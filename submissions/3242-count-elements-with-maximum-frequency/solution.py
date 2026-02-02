class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = defaultdict(int)
        for n in nums:
            frequencies[n] += 1
        
        max_times = 0
        max_feq = 0
        for feq in frequencies.values():
            if feq > max_feq:
                max_feq = feq
                max_times = 1
            elif feq == max_feq:
                max_times += 1
        return max_times * max_feq
        
