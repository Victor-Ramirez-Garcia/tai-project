#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        int n = nums.size();
        // Create an array of pairs: {element_value, original_index}
        vector<pair<int, int>> indexed_nums(n);
        for (int i = 0; i < n; ++i) {
            indexed_nums[i] = {nums[i], i};
        }

        // Partially sort to find the top k largest elements based on their values.
        // We sort in descending order of values.
        nth_element(indexed_nums.begin(), indexed_nums.begin() + k, indexed_nums.end(), 
                    [](const pair<int, int>& a, const pair<int, int>& b) {
                        return a.first > b.first;
                    });

        // Keep only the top k largest elements
        indexed_nums.resize(k);

        // Sort the chosen k elements based on their original indices to maintain subsequence order
        sort(indexed_nums.begin(), indexed_nums.end(), 
             [](const pair<int, int>& a, const pair<int, int>& b) {
                 return a.second < b.second;
             });

        // Extract the values into the final result array
        vector<int> result(k);
        for (int i = 0; i < k; ++i) {
            result[i] = indexed_nums[i].first;
        }

        return result;
    }
};