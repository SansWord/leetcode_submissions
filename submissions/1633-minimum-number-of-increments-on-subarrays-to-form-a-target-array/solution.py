class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        total = 0

        pre = 0

        for num in target:
            if num > pre:
                total += num - pre
            pre = num


        return total
        
