#include <algorithm>
using namespace std;

class Solution {
public:

    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int ans = 0;
        vector<vector<int>> tallest(m, vector<int>(n));
            
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && matrix[0][j] == 1) {
                    tallest[0][j] = 1;
                } else if (matrix[i][j] == 1) {
                    tallest[i][j] = 1 + tallest[i-1][j];
                }
            }
        }

        for (int i = 0; i < m; i++) {
            int max_of_row_i = 0;
            sort(tallest[i].begin(), tallest[i].end());

            for (int j = 0; j < n; j++) {
                if (tallest[i][j] * (n - j) > max_of_row_i)
                    max_of_row_i = tallest[i][j] * (n - j);
            }
            if (max_of_row_i > ans) 
                ans = max_of_row_i;
        } 

        return ans;
    }
};
