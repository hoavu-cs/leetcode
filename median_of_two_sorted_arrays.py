import math

class Solution:
    def findMedianSortedArray(self, nums):
        n = len(nums)
        if n % 2 == 0:
            return (nums[int(n/2)-1]+nums[int(n/2)])/2
        else:
            return nums[int(n/2)]

    def findLowHighPoints(self, n):
        if n % 2 == 0:
            return (int(n/2)-5, int(n/2)+4)
        else:
            return (int(n/2)-5, int(n/2)+5)
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        if n <= 10 and m <= 10:
            nums3 = nums1 + nums2
            nums3.sort()
            return self.findMedianSortedArray(nums3)
        elif n <= 10:
            x = self.findLowHighPoints(m)
            low = x[0]
            high = x[1]
            nums3 = nums1 + nums2[low:high+1]
            nums3.sort()
            return self.findMedianSortedArray(nums3)        
        elif m <= 10:
            x = self.findLowHighPoints(n)
            low = x[0]
            high = x[1]
            nums3 = nums2 + nums1[low:high+1]
            nums3.sort()
            return self.findMedianSortedArray(nums3)     
        else:
            a = self.findMedianSortedArray(nums1)
            b = self.findMedianSortedArray(nums2)
            if a == b:
                return a
            elif a > b:
                k = min(n - math.ceil(n/2) - 3, math.floor(m/2) - 3)
                return self.findMedianSortedArrays(nums1[:n-k], nums2[k:])
            else:
                k = min(m - math.ceil(m/2) - 3, math.floor(n/2) - 3)
                return self.findMedianSortedArrays(nums2[:m-k], nums1[k:])