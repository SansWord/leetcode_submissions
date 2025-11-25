class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        ones = []
        twos = []

        total = 0
        
        for i in nums:
            total += i

            if i % 3 == 1:
                ones.append(i)
            elif i % 3 == 2:
                twos.append(i)

        remainder = total % 3
        if remainder == 0:
            return total
        
        if remainder == 1:
            # remove 1 from ones or 2 from twos, pick smaller
            if len(ones) == 0 and len(twos) < 2:
                return 0
            one_removed = 0
            two_removed = 0

            if len(ones) > 0:
                one_removed = total - ones[0]
            if len(twos) >= 2:
                two_removed = total - twos[0] - twos[1]
            
            return max(one_removed, two_removed)
            
        
        if remainder == 2:
            # remove 1 from twos or 2 from ones, pick smaller
            if len(twos) == 0 and len(ones) < 2:
                return 0
            one_removed = 0
            two_removed = 0

            if len(ones) >= 2:
                one_removed = total - ones[0] - ones[1]
            if len(twos) > 0:
                two_removed = total - twos[0]
            
            return max(one_removed, two_removed)
