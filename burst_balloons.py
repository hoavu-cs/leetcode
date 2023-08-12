import numpy as np

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Dynamic programming solution
        # dp[i...j] = max. num of coins getting by popping balloons i to j.
        # Consider k: i <= k <= j be the last balloon popped.
        # dp[i...j] = max_k dp[i...k-1] + dp[k+1...j] + nums[k]
        
        # pad 1 at the beginning and the end
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)

        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        dp[0][0] = nums[1]
        dp[n+1][n+1] = nums[n]
        for i in range(1, n+1):
            dp[i][i] = nums[i-1]*nums[i]*nums[i+1]

        for k in range(1, n):
            for i in range(1, n+1-k):
                right = i+k
                for j in range(i, right+1):
                    if dp[i][j-1] + dp[j+1][right] + nums[i-1]*nums[j]*nums[right+1] > dp[i][right]:
                        dp[i][right] = dp[i][j-1] + dp[j+1][right] + nums[i-1]*nums[j]*nums[right+1]
        return dp[1][n]