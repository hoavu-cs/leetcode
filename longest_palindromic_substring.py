class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True for j in range(n)] for i in range(n)]
        output = s[0]
        for k in range(1, n):
            for i in range(n-k):
                end = i+k
                if s[i] == s[end]:
                    dp[i][end] = dp[i+1][end-1]
                    if dp[i][end]: output = s[i: end+1]
                else:
                    dp[i][end] = False
        return output

        