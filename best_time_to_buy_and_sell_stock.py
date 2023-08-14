from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        min_so_far = prices[0]
        max_profit = 0

        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_so_far)
            min_so_far = min(min_so_far, prices[i]) 

        return max_profit
