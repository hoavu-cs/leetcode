from math import inf

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left_closest = [inf for _ in range(len(seats))]
        right_closest = [inf for _ in range(len(seats))]
        
        if seats[0] == 1:
            left_closest[0] = 0
        if seats[n-1] == 1:
            right_closest[n-1] = 0

        dist = 0
        for i in range(1, n):
            if seats[i] == 1:
                left_closest[i] = 0
            else:
                left_closest[i] = left_closest[i - 1] + 1

        dist = 0
        for i in range(n-2, -1, -1):
            if seats[i] == 1:
                right_closest[i] = 0
            else:
                right_closest[i] = right_closest[i + 1] + 1

        closest = [min(left_closest[i], right_closest[i]) for i in range(len(seats))]
        return max(closest)
            

         
