#include <cmath>

const int inf = pow(10,5) + 1;

class Solution {
public:
    int maxProfit(vector<int>& prices) {

      int n = prices.size(), max_profit = 0;
      vector<int> dp1 (n + 2, 0), dp2 (n + 2, 0); 
      vector<int> min_prefix (n + 2, 0), max_suffix(n + 2, 0);
      prices.insert(prices.begin(), inf);
      prices.push_back(-inf);

      min_prefix[0] = inf;
      max_suffix[n + 1] = -inf;
      dp1[0] = -inf;
      dp2[n + 1] = -inf;

      for (int i = 1; i <= n; i++) {
        if (prices[i] < min_prefix[i - 1]) {
          min_prefix[i] = prices[i];
        } else {
          min_prefix[i] = min_prefix[i - 1];
        }
        dp1[i] = max(dp1[i - 1], prices[i] - min_prefix[i - 1]);
        max_profit = max(max_profit, dp1[i]);
      }

      for (int i = n; i >= 1; i--) {
        if (prices[i] > max_suffix[i + 1]) {
          max_suffix[i] = prices[i];
        } else {
          max_suffix[i] = max_suffix[i + 1];
        }
        dp2[i] = max(dp2[i + 1], max_suffix[i + 1] - prices[i]);
        max_profit = max(max_profit, dp2[i]);
      }

      for (int i = 2; i <= n - 2; i++) {
        max_profit = max(max_profit, dp1[i] + dp2[i+1]);
      }

      return max_profit;
    }
};
