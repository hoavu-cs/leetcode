class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_behind_cost = 0
        one_behind_cost = 0
        current_cost = 0
        for i in range(2, len(cost)+1):
            current_cost = min(two_behind_cost + cost[i-2], one_behind_cost + cost[i-1])
            two_behind_cost = one_behind_cost
            one_behind_cost = current_cost
        return current_cost
