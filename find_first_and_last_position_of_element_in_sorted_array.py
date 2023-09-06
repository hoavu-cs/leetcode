class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n-1
        first, last = -1, -1

        if n == 0:
            return [-1, -1]

        # binary search for the first occurence of target
        while i < j:
            m = (i + j)//2
            if target <= nums[m]:
                j = m
            else:
                i = m + 1
        if nums[i] == target:
            first = i
        
        i, j = 0, n-1
        # binary search for the last occurence of target
        while i < j:
            m = (i + j)//2 + 1
            if target >= nums[m]:
                i = m
            else:
                j = m - 1
        if nums[i] == target:
            last = i

        return [first, last]
        
