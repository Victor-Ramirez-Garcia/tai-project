#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        int n = nums.size();
        // Create an array of indices [0, 1, ..., n-1]
        vector<int> indices(n);
        iota(indices.begin(), indices.end(), 0);
        
        // Find the k indices corresponding to the k largest elements.
        // We use stable_sort or nth_element. To ensure O(N) average time complexity,
        // nth_element is preferred. We sort indices based on their values in nums in descending order.
        nth_element(indices.begin(), indices.begin() + k, indices.end(), [&](int a, int b) {
            return nums[a] > nums[b];
        });
        
        // Resize indices to only keep the top k elements
        indices.resize(k);
        
        // Sort these top k indices in ascending order to preserve the original subsequence order
        sort(indices.begin(), indices.end());
        
        // Build the result subsequence using the sorted indices
        vector<int> result;
        result.reserve(k);
        for (int idx : indices) {
            result.push_back(nums[idx]);
        }
        
        return result;
    }
};