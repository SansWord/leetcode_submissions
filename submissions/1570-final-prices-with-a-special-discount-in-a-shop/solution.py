class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [-1 for n in prices]
        stack = []
        # iterate backward

        for i in range(len(prices)-1, -1, -1):
            curr = prices[i]
            while stack and stack[-1] > curr:
                stack.pop()

            if not stack:
                ans[i] = curr
            else:
                ans[i] = curr - stack[-1]
            
            stack.append(curr)

        return ans


        
