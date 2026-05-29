#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        // Pairs of {element_value, original_index}
        vector<pair<int, int>> val_idx;
        val_idx.reserve(nums.size());
        
        for (int i = 0; i < nums.size(); ++i) {
            val_idx.push_back({nums[i], i});
        }
        
        // Find the k largest elements. We can use nth_element to do this in O(N) average time.
        // We partition the array so that the largest k elements are at the beginning.
        nth_element(val_idx.begin(), val_idx.begin() + k, val_idx.end(), 
                    [](const pair<int, int>& a, const pair<int, int>& b) {
                        return a.first > b.first; // Sort descending by value
                    });
        
        // Sort the first k elements based on their original indices to maintain subsequence order.
        // This takes O(k log k) time.
        sort(val_idx.begin(), val_idx.begin() + k, 
             [](const pair<int, int>& a, const pair<int, int>& b) {
                 return a.second < b.second; // Sort ascending by index
             });
        
        // Collect the values of the top k elements in their original relative order.
        vector<int> result;
        result.reserve(k);
        for (int i = 0; i < k; ++i) {
            result.push_back(val_idx[i].first);
        }
        
        return result;
    }
};