class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i, x in enumerate(nums[1:], 1):
            dp[i] = max(dp[i-1]+x, x)
        return max(dp)
        