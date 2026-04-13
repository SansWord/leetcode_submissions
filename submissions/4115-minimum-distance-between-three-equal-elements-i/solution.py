class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        numToIdxes = defaultdict(list)

        for i, num in enumerate(nums):
            numToIdxes[num].append(i)

        minDist = float("inf")
        
        for idxes in numToIdxes.values():
            if len(idxes) < 3:
                continue
            
            for i in range(len(idxes)-2):
                # abs(k-j) + abs(k-i) + abs(j-i) = 2 * (k-i)
                dist = 2 * (idxes[i+2]-idxes[i])
                if dist < minDist:
                    minDist = dist

        return minDist if minDist != float("inf") else -1

        
