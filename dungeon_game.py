from math import inf

class Solution:
            
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        ans = 0

        dp = [[inf for j in range(n)] for i in range(m)]
        if dungeon[m - 1][n - 1] < 0:
            dp[m - 1][n - 1] = -dungeon[m - 1][n - 1] + 1 
        else:
            dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                if i == m - 1:
                    dp[i][j] = max(dp[i][j + 1] - dungeon[i][j], 1)
                elif j == n - 1:
                    dp[i][j] = max(dp[i + 1][j] - dungeon[i][j], 1)
                else:
                    dp[i][j] = max(min(dp[i][j + 1] - dungeon[i][j], dp[i + 1][j] - dungeon[i][j]), 1)

        return dp[0][0]
