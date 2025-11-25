class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = float("inf")
        for i in nums: 
            if i == 1:
                if dist < k:
                    return False
                else:
                    dist = 0
            else:
                dist += 1

        return True
        
