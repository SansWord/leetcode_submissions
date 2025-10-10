class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pre_state=[0, -prices[0]]
        curr_state=[0, -prices[0]]

        state_no = 0
        state_bought = 1

        for i in range(1, len(prices)):
            curr_state[state_no] = max(pre_state[state_no], pre_state[state_bought] + prices[i] - fee)
            curr_state[state_bought] = max(pre_state[state_no] - prices[i], pre_state[state_bought])

            pre_state[state_no] = curr_state[state_no]
            pre_state[state_bought] = curr_state[state_bought]

        return max(curr_state)

        
