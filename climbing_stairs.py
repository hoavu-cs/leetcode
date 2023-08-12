class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1: return 1
        if n == 2: return 2
        two_behind = 1
        one_behind = 2
        current = 0
        for i in range(3, n+1):
            current = two_behind + one_behind 
            two_behind = one_behind
            one_behind = current
        return current

