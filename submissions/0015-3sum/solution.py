class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        # construct a value to position map in O(n) for later usage
        # key: value of nums, v
        # value: list of position p such that nums[p] == v
        number_position = {}
        for i, v in enumerate(nums):
            if v not in number_position:
                number_position[v] = [i]
            else:
                number_position[v].append(i)


        result = []
        preFirst = None
                
        for i, first in enumerate(nums[:-2]):
            if preFirst == first:
                continue

            preFirst = first


            preSecond = None
            for j in range(i+1, len(nums)):
                second = nums[j]
                if preSecond == second:
                    continue
                
                preSecond = second

                third = (-first - nums[j])
                if third in number_position and number_position[third][-1] > j:
                    result.append([first, second, third])

        return result


