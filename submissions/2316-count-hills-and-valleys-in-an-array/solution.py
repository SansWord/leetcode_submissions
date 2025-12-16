class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        pre = nums[0]
        i = 1
        res = 0
        while i < len(nums) - 1:
            curr = nums[i]
            if curr == pre:
                i += 1
            else:
                postIdx = i + 1
                # find next number that is not equal to curr
                while postIdx < len(nums) and nums[postIdx] == curr:
                    postIdx+= 1
                
                # no such number, exit while_loop
                if postIdx == len(nums):
                    break
                
                # found post != curr, check if curr is hill/valley
                post = nums[postIdx]
                if (curr < post and curr < pre) or (curr > post and curr > pre):
                    res += 1

                
                # next iteration
                pre = curr
                i = postIdx
        
        return res

        
