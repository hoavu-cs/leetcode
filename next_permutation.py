from math import inf
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def suffix_bubble_sort(A, k):
            for i in range(k, len(A)):
                for j in range(i + 1, len(A)):
                    if A[j] < A[i]:
                        A[i], A[j] = A[j], A[i]

        n = len(nums)
        smallest_idx = n - 1

        for i in range(n-2, -1, -1):
            swap_idx = -1
            next_smallest = inf
            for j in range(i + 1, n):
                if nums[i] < nums[j] and nums[j] < next_smallest:
                    next_smallest, swap_idx = nums[j], j
            if swap_idx != -1:
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
                suffix_bubble_sort(nums, i + 1)
                return

        suffix_bubble_sort(nums, 0)





    

        
