from math import log, ceil, floor

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Each pig can die on the ith round where 1 <= i <= n_rounds or may not die.
        # There can be at most buckets configuration to encode.

        n_rounds = floor(minutesToTest/minutesToDie)
        ans = 0
        while (n_rounds + 1) ** ans < buckets:
            ans += 1
        return ans
