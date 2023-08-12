from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[inf for j in range(amount+1)] for i in range(n)]
        
        dp[0][0] = 0
        for j in range(1, amount+1):
            if j >= coins[0]:
                dp[0][j] = dp[0][j-coins[0]]+1

        for i in range(1, n):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 0
                elif j >= coins[i]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]]+1)
                else:
                    dp[i][j] = dp[i-1][j]
                                        
        return -1 if dp[n-1][amount] == inf else dp[n-1][amount]
