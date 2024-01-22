class Solution {

public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        if (nums.size() == 1 && nums[0] >= lower && nums[0] <= upper) {
            return 1;
        } else if (nums.size() == 1) {
            return 0;
        } 

        long mid = static_cast<long> (nums.size() / 2), ans = 0;
        long idx_1, idx_2;
        vector<int> left_half(nums.begin(), nums.begin() + mid);
        vector<int> right_half(nums.begin() + mid, nums.end());

        // recursively count the left half and right half
        ans += countRangeSum(left_half, lower, upper);
        ans += countRangeSum(right_half, lower, upper);

        // count the number of [lower, upper] range sums that cross the mid point
        vector<long> left_sums, right_sums;
        long left_accumulation = 0, right_accumulation = 0;


        for (int i = mid - 1; i >= 0; i--) {
            left_accumulation += nums[i];
            left_sums.push_back(left_accumulation);
        }

        for (int i = mid; i < nums.size(); i++) {
            right_accumulation += nums[i];
            right_sums.push_back(right_accumulation);
        }

        sort(right_sums.begin(), right_sums.end());

        for (size_t i = 0; i < left_sums.size(); i++) {
            idx_1 = lower_bound(right_sums.begin(), right_sums.end(), lower - left_sums[i]) - right_sums.begin();
            idx_2 = upper_bound(right_sums.begin(), right_sums.end(), upper - left_sums[i]) - right_sums.begin();
            ans += idx_2 - idx_1;
        }

        return ans;
    }
};
