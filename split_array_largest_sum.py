from math import inf

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.insert(0, 0)

        sums = [0 for i in range(n+1)]
        sums[0] = nums[0]
        for i in range(n+1):
            sums[i] = sums[i-1] + nums[i]

        dp = [[inf for i in range(n+1)] for j in range(k+1)]

        for j in range(1, k+1):
            for i in range(1, n+1):
                if i > j:
                    dp[j][i] = inf
                if j == 1:
                    dp[j][i] = sums[i]

        for j in range(2, k+1):
            for i in range(j, n+1):
                for l in range(j-1, i):
                    dp[j][i] = min(dp[j][i], max(dp[j-1][l], sums[i]-sums[l]))
        return dp[k][n]
