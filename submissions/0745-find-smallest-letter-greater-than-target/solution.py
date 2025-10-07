class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo = 0
        hi = len(letters)
        targetIdx = 0
        while lo < hi:
            mid = (lo + hi)//2

            curr = letters[mid]

            # find curr < target
            if ord(target) >= ord(curr):
                lo = mid + 1
            else:
                targetIdx = mid
                hi = mid

        return letters[targetIdx]
        
