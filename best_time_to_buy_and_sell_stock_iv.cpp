const int inf = pow(10,5) + 1;

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size(), max_profit = 0;
        vector<vector<vector<int>>> dp(n, vector<vector<int>> (k + 1, vector<int> (4, 0)));
        
        // dp[i][j][l]: l = 0: holding stock, l = 1: not holding, l = 2: selling, l = 3: buying
        // i: day, j: number of completed buy & sell
        dp[0][0][0] = -inf;
        dp[0][0][1] = 0;
        dp[0][0][2] = -inf;
        dp[0][0][3] = -prices[0];

        for (int j = 1; j <= k; j++) {
            dp[0][j][0] = -inf;
            dp[0][j][1] = -inf;
            dp[0][j][2] = -inf;
            dp[0][j][3] = -inf;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][3]);

                if (j > 0)
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][2]);
                else
                    dp[i][j][1] = dp[i - 1][j][1];
                
                if (j > 0)
                    dp[i][j][2] = max(prices[i] + dp[i - 1][j - 1][0], prices[i] + dp[i - 1][j - 1][3]);

                dp[i][j][3] = max(dp[i - 1][j][1] - prices[i], dp[i - 1][j][2] - prices[i]);
                max_profit = max(max_profit, dp[i][j][2]);   
            }
        }
        
        return max_profit;
    }
};
