class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        size = len(nums)
        seen = [False for i in range(size)]
        checked = set()

        for i in range(size):
            if seen[i]:
                continue

            walked = set()
            curr = i
            while curr not in walked:
                seen[curr] = True
                walked.add(curr)
                curr = (curr + nums[curr] + size) % size
            target = curr

            if not target in checked:
                checked.add(target)
                # checking if target can have a loop
                if self.isLooping(nums, target):
                    print(target)
                    return True

        
        return False

    def isLooping(self, nums: List[int], start: int) -> bool:
        size = len(nums)
        numNodes = 1
        firstStep = nums[start]
        curr = (start + firstStep + size) % size
        isFirstStepNegative = firstStep < 0

        while curr != start:
            step = nums[curr]

            if isFirstStepNegative != (step < 0):
                # not consistist with all the same sign
                return False

            curr = (curr + step + size) % size
            numNodes += 1


        return numNodes > 1
        
