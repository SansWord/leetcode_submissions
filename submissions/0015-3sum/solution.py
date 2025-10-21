class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        LEN = len(nums)
        nums.sort()
        result = []

        pre = None
        for i, num in enumerate(nums[:-2]):
            if num != pre:
                twoSum = self.twoSum(nums, i+1, LEN-1, -num)
                for pair in twoSum:
                    result.append([num] + pair)
                pre = num

        return result

    def twoSum(self, nums: list[int], start: int, end: int, target: int) -> List[List[int]]:
        result = []
        l = start
        r = end

        while l < r:
            lVal = nums[l]
            rVal = nums[r]
            localSum = lVal + rVal
            if localSum == target:
                result.append([lVal, rVal])
                # add l until lVal is different
                while l < r and nums[l] == lVal:
                    l += 1
            
            elif localSum < target:
                l += 1
            else:
                r -= 1
        
        return result


