from math import inf

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        it1 = it2 = it3 = 0

        for i in range(m-1, -1, -1):
            nums1[n+i] = nums1[i]

        while it1 < m or it2 < n:
            x1 = x2 = inf
            if it1 < m: x1 = nums1[n+it1]
            if it2 < n: x2 = nums2[it2]
            if x1 < x2:
                nums1[it3] = x1
                it3 += 1
                it1 += 1
            else:
                nums1[it3] = x2
                it3 += 1
                it2 += 1
                
