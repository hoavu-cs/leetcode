class Solution {
public:
    bool isMatch(string s, string p) {
        size_t m = s.length(), n = p.length();
        vector<vector<bool>> dp(m, vector<bool> (n, false));

        if (m == 0) {
            return (p.find_first_not_of('*') == string::npos);
        } else if (n == 0) {
            return false;
        }

        for (size_t i = 0; i < m; i++) {
            for (size_t j = 0; j < n; j++) {
                if (i == 0) {
                    int count1 = 0, count2 = 0, count3 = 0;

                    for (size_t k = 0; k <= j; k++) {
                        if (p[k] == s[0]) {
                            count1++;
                        } else if (p[k] == '*') {
                            count2++;
                        } else if (p[k] == '?') {
                            count3++;
                        } 
                    }

                    if (count2 == j + 1) {
                        dp[i][j] = true;
                    } else if (count1 + count3 == 1 && count2 == j) {
                        dp[i][j] = true;
                    }
                    
                } else if (j == 0) {
                    if (p[j] == '*') {
                        dp[i][j] = true; // * can match any prefix
                    } else if (p[j] == '?') {
                        dp[i][j] = (i == 0); // ? can match any single char
                    } else {
                        dp[i][j] = (i == 0) && (s[i] == p[j]); // otherwise, 2 single chars must match
                    }
                } else if (p[j] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j] == '*') {
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
                } else {
                    dp[i][j] = (s[i] == p[j]) && dp[i - 1][j - 1];
                }
            }
        } 

        return dp[m - 1][n - 1];
    }
};
