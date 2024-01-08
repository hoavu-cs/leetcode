from math import inf 

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i, j, window_sum = 0, -1, 0
        ans = inf

        while i < n:
            while j < n - 1 and window_sum < target:
                j += 1
                window_sum += nums[j]

            if window_sum >= target and j - i + 1 < ans:
                ans = j - i + 1

            window_sum -= nums[i]
            i += 1
 
        return 0 if ans == inf else ans 

        
