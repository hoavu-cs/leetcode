class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {

        multiset<int> window;

        for (size_t i = 0; i <= min(indexDiff, (int)nums.size() - 1); i++) {
            window.insert(nums[i]);
        }

        for (auto it = next(window.begin()); it != window.end(); it++) {
            if (*it - *prev(it) <= valueDiff) {
                return true;
            }
        }

        for (size_t i = indexDiff + 1; i < nums.size(); i++) {
            window.erase(nums[i - indexDiff - 1]);
            window.insert(nums[i]);
            auto it = window.find(nums[i]);

            if (it == window.begin()) {
                if (*next(it) - *it <= valueDiff) {
                    return true;
                } 
            } else if (it == prev(window.end())) {
                if (*it - *prev(it) <= valueDiff) {
                    return true;
                } 
            } else {
                if ((*next(it) - *it <= valueDiff) || (*it - *prev(it) <= valueDiff)) {
                    return true;
                }
            }
        }

        return false;
    }
};
