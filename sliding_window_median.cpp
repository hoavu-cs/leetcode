#include<algorithm>
#include <random>

class Solution {
private:
    void removeHelper(std::priority_queue<long double>& q, std::set<long double>& removed, bool is_max_heap) {
        if (is_max_heap) {
            while (q.size() > 0 && removed.find(q.top()) != removed.end()) {
                q.pop();
            }
        } else {
            while (q.size() > 0 && removed.find(-q.top()) != removed.end()) {
                q.pop();
            }
        }
    }

public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        size_t n = nums.size();
        std::vector<long double> A(n, 0);
        std::mt19937_64 rng(std::random_device{}());

        // Uniform distribution in range [0, 1)
        std::uniform_real_distribution<double> dist(0.0, 1e-8);

        for (size_t i = 0; i < n; i++) {
            // add a small amount to avoid duplicates
            A[i] = static_cast<long double>(nums[i]) + dist(rng);
        }

        // left contains all elements < median 
        // right contains all elements > median
        std::priority_queue<long double> left, right;
        std::set<long double> removed;
        std::vector<long double> ans;
        std::vector<long double> first_window(A.begin(), A.begin() + k);
        long double median;

        std::sort(first_window.begin(), first_window.end());

        if (k % 2 == 1) {
            median = first_window[k/2];
        } else {
            median = (first_window[k/2 - 1] + first_window[k/2])/2;
        }

        ans.push_back(median);

        for (size_t i = 0; i < k; i++) {
            if (A[i] < median) {
                left.push(A[i]);
            } else if (A[i] > median) {
                right.push(-A[i]);
            }
        }

        for (size_t i = k; i < n; i++) {
            removed.insert(A[i - k]);

            if ((A[i] > median && A[i - k] > median) || 
                (A[i] < median && A[i - k] < median)) {
                // median stays the same in the new window
                if (A[i] > median) {
                    right.push(-A[i]);
                    removeHelper(right, removed, false);

                    if (k % 2 == 0) {
                        median =  (left.top() - right.top())/2;
                    }
                } else {
                    left.push(A[i]);
                    removeHelper(left, removed, true);

                    if (k % 2 == 0) {
                        median =  (left.top() - right.top())/2;
                    }
                }
            }  else if (A[i] > median && A[i - k] == median) {
                right.push(-A[i]);
                // k must be odd
                median = -right.top();
                right.pop();
            } else if (A[i] < median && A[i - k] == median) {
                left.push(A[i]);
                // k must be odd
                median = left.top();
                left.pop();
            } else if (A[i] > median && A[i - k] < median) {
                right.push(-A[i]);

                if (k % 2 == 1) {
                    left.push(median);
                    removeHelper(right, removed, false);
                    median = -right.top();
                    right.pop();    
                    removeHelper(right, removed, false);            
                } else {
                    removeHelper(right, removed, false);
                    left.push(-right.top());
                    right.pop();
                    removeHelper(right, removed, false);
                    median =  (left.top() - right.top())/2;
                }
            } else if (A[i] < median && A[i - k] > median) {
                left.push(A[i]);

                if (k % 2 == 1) {
                    right.push(-median);
                    removeHelper(left, removed, true);
                    median = left.top();
                    left.pop();
                    removeHelper(left, removed, true);
                } else {
                    removeHelper(left, removed, true);
                    right.push(-left.top());
                    left.pop();
                    removeHelper(left, removed, true);
                    
                    median = static_cast<long double> ((left.top() - right.top())/2);        
                }
            }
            ans.push_back(median);
        }

        vector<double> ret;
        for (const auto& elm : ans) {
            ret.push_back(static_cast<double> (elm));
        }
        return ret;
    }
};
