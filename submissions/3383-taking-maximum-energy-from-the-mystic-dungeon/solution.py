class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        LEN = len(energy)
        result = [0] * k

        for i in range(LEN):
            e = energy[i]
            bucket = i % k

            # add into kth bucket
            result[bucket] += e

            # if this cause result to be negative, and there could be another magician, 
            # drop the result, means skipping all visited migician of this bucket.
            if result[bucket] < 0 and i < LEN-k:
                result[bucket] = 0
        
        return max(result)

