class Solution {
private:
    int closest_binary_search(vector<int>& nums, size_t left, size_t right, int target) {
        size_t left_boundary = left, right_boundary = right;
        int ans = nums[left];

        while (left < right) {
            size_t mid = left + (right - left)/2;

            if (nums[mid] == target) {
                return target;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        for (size_t i = left - 1; i <= left + 1; i++) {
            if (i >= left_boundary && i <= right_boundary) {
                if (abs(target - nums[i]) < abs(target - ans)) {
                    ans = nums[i];
                }
            }
        }

        return ans;
    }

public:
    int threeSumClosest(vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        int ans = nums[0] + nums[1] + nums[2];

        for (size_t i = 0; i < nums.size() - 2; i++) {
            for (size_t j = i + 1; j < nums.size() - 1; j++) {       
                int remaining_target = target - nums[i] - nums[j];
                int closest_remaining = closest_binary_search(nums, j + 1, nums.size() - 1, remaining_target);

                if (abs(nums[i] + nums[j] + closest_remaining - target) < abs(ans - target)) {
                    ans = nums[i] + nums[j] + closest_remaining;
                }
            }
        }

        return ans;
    }
};
