#include<algorithm>
using namespace std;

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {

        if (points.size() == 1)
            return 1;
        else if (points.size() == 0)
            return 0;

        int n = points.size(), ans = 0;
        map<float, vector<vector<int>>> tan_table;
        vector<vector<int>> inf_tan_table;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (points[j][0] - points[i][0] == 0) {
                    inf_tan_table.push_back({i, j});
                } else {
                    float tan = (float)(points[j][1] - points[i][1])/(points[j][0] - points[i][0]);
                    tan_table[tan].push_back({i, j});
                }
            }
        }

        for (auto& x : tan_table) {
            vector<vector<int>>& pairs = x.second;
            map<int, int> colinear_points;
            for (auto& it : pairs) {
                colinear_points[it[0]]++;
                if (colinear_points[it[0]] + 1 > ans)
                    ans = colinear_points[it[0]] + 1;
            }   
        }

        map<int, int> vertical_colinear_points;
        for (auto& it : inf_tan_table) {
            vertical_colinear_points[it[0]]++;
            if (vertical_colinear_points[it[0]] + 1 > ans)
                ans = vertical_colinear_points[it[0]] + 1;
        }

        return ans;
    }
};
