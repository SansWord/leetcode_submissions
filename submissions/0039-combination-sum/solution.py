class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.helper(candidates, target)
    
    def helper(self, sortedCandidates: list[int], target: int) -> list[list[int]]:
        if target == 0:
            return [ [] ]

        if len(sortedCandidates) == 0:
            return []

        curr = sortedCandidates[0]
        if curr > target:
            return []
        
        if curr == target:
            return [ [curr] ]

        pick_n = target // curr
        picked = []
        result = []
        # picked curr for i times, until pick_n times
        for i in range(pick_n + 1):
            rests = self.helper(sortedCandidates[1:], target - i * curr)
            for rest in rests:
                result.append(picked + rest)
            picked.append(curr)
        
        return result

        
