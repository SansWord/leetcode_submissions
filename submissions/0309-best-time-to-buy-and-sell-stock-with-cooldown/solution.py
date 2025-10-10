class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        
        pre_states = [-1, -1, -1]
    
        state_no_stock = 0
        state_bought = 1
        state_sold = 2

        pre_states[state_no_stock] = 0
        pre_states[state_bought] = -prices[0]
        pre_states[state_sold] = 0

        curr_states = [0, 0, 0]
        for i in range(1, length):
            

            curr_states[state_no_stock] = max(pre_states[state_no_stock], pre_states[state_sold])
            curr_states[state_bought] = max(pre_states[state_bought], pre_states[state_no_stock] - prices[i])
            curr_states[state_sold] = pre_states[state_bought] + prices[i]

            pre_states[state_no_stock] = curr_states[state_no_stock]
            pre_states[state_bought] = curr_states[state_bought]
            pre_states[state_sold] = curr_states[state_sold]

        
        return max(curr_states)

