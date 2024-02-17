class Solution {
private:
    void monotonicStackPush(list<int>& S, int x) {
        while (!S.empty() && x < S.back()) {
            S.pop_back();
        } 
        S.push_back(x);
    }

public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        list<int> S;
        vector<int> ans; 
        size_t n = nums.size();

        for (size_t i = 0; i <= n - k; i++) {
            monotonicStackPush(S, nums[i]);
        }
        ans.push_back(S.front());
        S.pop_front();

        for (size_t t = 2; t <= k; t++) {
            monotonicStackPush(S, nums[n - k + t - 1]);
            ans.push_back(S.front());
            S.pop_front();
        }

        return ans;
    }
};
