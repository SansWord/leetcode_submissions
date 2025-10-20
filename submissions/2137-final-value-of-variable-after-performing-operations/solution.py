class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        values = {
            "--X": -1,
            "++X": 1,
            "X++": 1,
            "X--": -1
        }
        
        res = 0
        for operation in operations:
            res += values[operation]
        
        return res
        
