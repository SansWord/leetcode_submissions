class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        occurrence = defaultdict(int)
        for i in range(k):
            occurrence[nums[i]] += 1
        result.append(self.calculateXSum(occurrence, x))
        
        for i in range(k, len(nums)):
            outElm = nums[i-k]
            inElm = nums[i]
            print("==", i, outElm, inElm)
            if outElm == inElm:
                result.append(result[-1])
            else:
                occurrence[inElm] += 1
                occurrence[outElm] -= 1
                result.append(self.calculateXSum(occurrence, x))

        return result
    

    def calculateXSum(self, occurrence: dict[int, int], x: int) -> int:
        if len(occurrence.keys()) <= x:
            topKeys = occurrence.keys()
        else:
            k_v_pairs = []
            for k, v in occurrence.items():
                k_v_pairs.append((v, k))

            k_v_pairs.sort()
            print(occurrence, k_v_pairs)
            topKeys = {k for v, k in k_v_pairs[-x:]}

        res = 0
        for k in topKeys:
            res += occurrence[k] * k

        return res
