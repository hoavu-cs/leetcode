class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        if goal == 0:
            counter = ans = 0
            for i in range(n):
                if nums[i] == 0:
                    counter += 1
                else:
                    ans += counter * (counter + 1) / 2
                    counter = 0
            ans += counter * (counter + 1) / 2
            return int(ans)

        dp = [0 for i in range(n)]
        one_idx = []

        for i in range(n):
            if nums[i] == 1:
                one_idx.append(i)

        total = 0
        i = 0
        while i < n and total < goal:
            if nums[i] == 1:
                total += 1
            i += 1

        if total < goal:
            return 0

        dp[i - 1] = one_idx[0] + 1
        j = 0

        while i < n:
            if nums[i] == 0:
                dp[i] = dp[i - 1]
            else:
                j += 1
                dp[i] = one_idx[j] - one_idx[j - 1]  
            i += 1

        return sum(dp)



