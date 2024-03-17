class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        elif n == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        l = 0
        r = n - 1

        while r >= l + 2:
            mid = (l + r) // 2
            if nums[mid]  > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid
            elif nums[mid] < nums[mid - 1]:
                r = mid

        if r == 1:
            return 0
        else:
            return n - 1

        
