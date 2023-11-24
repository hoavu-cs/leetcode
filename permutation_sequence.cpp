#include <string>
#include <cmath>

using namespace std;

class Solution {
public:

    long factorial(int n) {
        long long ret = 1;
        for (int i = 2; i <= n; i++){
            ret = ret * i;
        }
        return ret;
    }

    void transform(string& s, vector<int>& elements) {
        sort(elements.begin(), elements.end());
        string ret = "";
        for (int i = 0; i < s.size(); i++){
            s[i] = elements[s[i] - '1'] + '0';
        }
    }

    void erase_value(vector<int>& array, int value){
        for (int i = 0; i < array.size(); i++){
            if (array[i] == value){
                array.erase(array.begin() + i);
                break;
            }
        }
    }

    string getPermutation(int n, int k) {
        int i = 1, j = 1;
        long k2;
        vector<int> remaining_elements = {};
        string ret = "";
        
        // find the length of the suffix that needs to be modified
        while (factorial(i) < k)
            i++;

        // keep track of all elements from 1-9 in the suffix
        for (int l = 1; l <= n; l++)
            remaining_elements.push_back(l);

        for(j = 1; j <= n - i; j++){
            ret = ret + to_string(j);
            remaining_elements.erase(remaining_elements.begin());
        }

        if (j == n) {
            // base case if suffix to be modified is empty (i.e., k = 1)
            ret = ret + to_string(j);
        } else {
            int adjust = ceil(static_cast<float> (k)/factorial(i - 1)) - 1;
            int remaining_k = k - adjust * factorial(i-1);

            j += adjust;
            ret = ret + to_string(j);
            erase_value(remaining_elements, j);

            string remaining_string = getPermutation(i - 1, remaining_k);
            transform(remaining_string, remaining_elements);

            ret = ret + remaining_string;
        }
        return ret;
    }
};
