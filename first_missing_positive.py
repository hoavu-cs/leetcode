from math import inf

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] > 0  and nums[i] != inf:
                origin = i 
                j = nums[i] - 1
                while j >= 0 and j < n and nums[j] != inf:
                    k = nums[j] - 1
                    nums[j] = inf 
                    j = k

        for i in range(n):
            if nums[i] != inf:
                return i + 1

        return n + 1

