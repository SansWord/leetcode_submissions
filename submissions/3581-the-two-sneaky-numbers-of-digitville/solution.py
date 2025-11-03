class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        found = 0
        result = []
        currIdx = -1
        while found < 2:
            curr = nums[currIdx]
            if nums[curr] == curr:
                result.append(curr)
                found += 1
                currIdx -= 1
            else:
                nums[currIdx], nums[curr] = nums[curr], curr
        return result
