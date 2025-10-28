class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        possibleSelections = []
        for i, num in enumerate(nums):
            if num == 0:
                possibleSelections.append(i)
        
        result = 0
        numsCopy = [num for num in nums]
        for selection in possibleSelections:
            for direction in [1, -1]:
                if self.testOperation(numsCopy, selection, direction):
                    result += 1
                for i in range(len(nums)):
                    numsCopy[i] = nums[i]
        return result

    
    def testOperation(self, nums, selection, movingDelta):

        curr = selection
        while curr >= 0 and curr < len(nums):
            currVal = nums[curr]
            if currVal > 0:
                nums[curr] -= 1
                movingDelta *= -1
            curr += movingDelta
        return all(val == 0 for val in nums)

        
