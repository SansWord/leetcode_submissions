class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 1
        digit = 1
        remainders = set()
        while curr % k != 0:
            if curr in remainders:
                return -1

            remainders.add(curr)
            curr = curr * 10 + 1
            curr %= k
            digit += 1

        return digit

