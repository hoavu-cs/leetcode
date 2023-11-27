class Solution {
public:
    unsigned int numDistinct(string s, string t) {
        int m = s.length(), n = t.length();
        vector<vector<unsigned int>> dp(m, vector<unsigned int>(n, 0));

        if (s[0] == t[0]) 
            dp[0][0] = 1;

        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i - 1][0];
            if (s[i] == t[0]) 
                dp[i][0]++;
        }

        for (int j = 1; j < n; j++) 
            dp[0][j] = 0;

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (s[i] == t[j])
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1];
                else
                    dp[i][j] = dp[i - 1][j];
            }
        }

        return dp[m - 1][n - 1];
    }
};
