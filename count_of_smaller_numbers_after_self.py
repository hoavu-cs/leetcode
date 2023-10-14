from bisect import bisect_right

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        else:
            m = len(nums)//2
            left, right = nums[:m], nums[m:]
            ans = self.countSmaller(left) + self.countSmaller(right)
            right_sorted = sorted(right)
            for idx, element in enumerate(left):
                k = bisect_left(right_sorted, element)
                ans[idx] += k
            return ans



