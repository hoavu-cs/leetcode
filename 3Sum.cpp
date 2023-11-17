#include <vector>
#include <algorithm>

using namespace std; 

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        vector<vector<int>> res;
        set<tuple<int, int, int>> triple_set;
        sort(nums.begin(), nums.end());

        if (nums.size() > 3) {
            vector<int> nums_deduplicated = {nums[0], nums[1], nums[2]};
            for (int i = 3; i < nums.size(); i++){
                if (nums[i] != nums[i-3]) {
                    nums_deduplicated.push_back(nums[i]);
                }
            }
            nums = nums_deduplicated;
        }

        for (int i = 0; i < nums.size() - 2; i++) {
            for (int j = i + 1; j < nums.size() - 1; j++){
                vector<int>::iterator startIterator = nums.begin() + j + 1;
                int target = 0 - nums[i] - nums[j];
                bool found = binary_search(startIterator, nums.end(), target);

                if (found){
                    vector<int> triple = {nums[i], nums[j], 0 - nums[i] - nums[j]};
                    tuple triple_tuple = make_tuple(nums[i], nums[j], 0 - nums[i] - nums[j]);
                    int count = triple_set.count(triple_tuple);
                    if (count == 0){
                        res.push_back(triple);
                        triple_set.insert(triple_tuple);
                    }
                }
            }
        }

        return res;
    }
};
