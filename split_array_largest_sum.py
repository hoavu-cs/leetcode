from math import inf

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def split_array_with_upper_bound(nums, k, upper_bound):
            if max(nums) > upper_bound:
                return False
            current_total = i = 0
            num_subarrays = 1
            for i in range(len(nums)):
                if current_total + nums[i] <= upper_bound:
                    current_total += nums[i]
                else:
                    current_total = nums[i]
                    num_subarrays += 1
                    if num_subarrays > k:
                        return False
            return True
            
        lower = 0
        upper = sum(nums)
        res = 0

        while upper > lower + 1:
            mid = int((lower+upper)/2)
            if split_array_with_upper_bound(nums, k, mid):
                upper = mid
            else:
                lower = mid
        
        if split_array_with_upper_bound(nums, k, lower):
            return lower
        else:
            return upper
            
