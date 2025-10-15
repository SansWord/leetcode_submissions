class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:

        N = len(nums)
        MOD = 10 ** 9 + 7

        ifactorial = [ pow(factorial(i), -1, MOD) for i in range(60) ]

        @cache
        def go(index, mleft, kleft, carry):
            if index == N:
                kleft -= carry.bit_count()
                if mleft == 0 and kleft == 0:
                    return 1
                else:
                    return 0
            
            total = 0
            # take index i times
            for i in range(mleft+1):
                # is bit being provided at this index position
                bit = (i+carry) % 2
                if kleft - bit >= 0:
                    total += pow(nums[index], i, MOD) * go(index+1, mleft-i, kleft-bit, (carry+i)//2) * ifactorial[i]
            
            return total % MOD
        
        return(go(0, m, k, 0) * factorial(m)) % MOD


