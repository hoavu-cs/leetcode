#include <cmath>

int inf = INFINITY;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> window = {inf};
        vector<int> ans;

        for (int i = 0; i < nums.size(); i++) {
            while (nums[i] > window.back()) 
                window.pop_back();
            window.push_back(nums[i]);
            
            if (i == k - 1) {
                ans.push_back(window[1]);
            } else if (i > k - 1) {
                if (nums[i - k] == window[1]) 
                    window.erase(window.begin() + 1);
                ans.push_back(window[1]);
            }
        }

        return ans;
    }
};
