from math import inf

class Solution:
    def binarySearch(self, nums, x):
        # return the first index that is strictly larger than x
        left = 0
        right = len(nums) - 1
        ans = inf

        while left <= right:
            m = (left + right) // 2
            if nums[m] <= x:
                left = m + 1
            else:
                if m < ans:
                    ans = m
                right = m - 1 

        return ans

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return 0, nums
        
        m = len(nums) // 2
        countLeft, left = self.mergeSort(nums[:m])
        countRight, right = self.mergeSort(nums[m:])
        ans = countLeft + countRight

        # aggregrate the number of reverse pairs
        for i, x in enumerate(right):
            smallestReverseIdx = self.binarySearch(left, 2 * x)
            if smallestReverseIdx != inf:
                ans += len(left) - smallestReverseIdx
        
        # merge two arrays 
        iLeft, iRight = 0, 0
        merge = []

        while iLeft < len(left) and iRight < len(right):
            if left[iLeft] <= right[iRight]:
                merge.append(left[iLeft])
                iLeft += 1
            else:
                merge.append(right[iRight])
                iRight += 1

        merge.extend(left[iLeft:])
        merge.extend(right[iRight:])

        return ans, merge

    def reversePairs(self, nums: List[int]) -> int:
        ans, A = self.mergeSort(nums)
        return ans 
