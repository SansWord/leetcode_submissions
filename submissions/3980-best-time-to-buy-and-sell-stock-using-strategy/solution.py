class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        length = len(prices)
        original_profits_prefix_sum = [-1] * (length+1)
        prices_prefix_sum = [-1] * (length+1)

        

        original_profits_prefix_sum[0] = 0
        prices_prefix_sum[0] = 0
        for i in range(length):
            original_profits_prefix_sum[i+1] = original_profits_prefix_sum[i] + prices[i] * strategy[i]
            prices_prefix_sum[i+1] = prices_prefix_sum[i] + prices[i]

    
        original_profit = original_profits_prefix_sum[-1]
        #print("original:", original_profit)
        max_profit = original_profit
        half_k = k // 2
        for i in range(0, length - k + 1):
            end = i + k
            mid = i + half_k
            original_profit_segment = original_profits_prefix_sum[end] - original_profits_prefix_sum[i]
            modified_profit_segment = prices_prefix_sum[end] - prices_prefix_sum[mid]
            
            new_profit = original_profit - original_profit_segment + modified_profit_segment
            #print(i, original_profit_segment, modified_profit_segment, new_profit)
            max_profit = max_profit if max_profit > new_profit else new_profit
            
        return max_profit

