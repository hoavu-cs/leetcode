class Solution:
    def canJump(self, nums: List[int]) -> bool:

        farthest_reachable_position = 0
        n = len(nums)
        for i in range(n):
            if i > farthest_reachable_position:
                return False
            else:
                if i + nums[i] >  farthest_reachable_position:
                    farthest_reachable_position = i + nums[i]
                if farthest_reachable_position >= n-1:
                    return True
        
        if farthest_reachable_position >= n-1:
            return True
        else:
            return False
        
