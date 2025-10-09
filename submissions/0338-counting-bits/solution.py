class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        result = [0,1]
        current_power_of_2 = 1

        for i in range(2, n+1):
            remain = i - current_power_of_2

            if remain == current_power_of_2:
                result.append(1)
                current_power_of_2 *= 2
            else:
                result.append(result[remain] + 1)

        return result

