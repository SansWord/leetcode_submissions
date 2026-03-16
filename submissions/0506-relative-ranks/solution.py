class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        LEN = len(score)
        score_idx = [ (-sc, idx) for idx, sc in enumerate(score) ]
        score_idx.sort()
        
        result = [""] * LEN

        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for idx, entry in enumerate(score_idx[0:3]):
            _, origin_idx = entry
            result[origin_idx] = medals[idx]

        if LEN > 3:
            for i in range(3, LEN):
                _, idx = score_idx[i]
                result[idx] = str(i+1)
        
        

        return result
        
