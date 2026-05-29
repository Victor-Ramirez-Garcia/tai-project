#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        // Algorithm: Sorting approach
        // Time Complexity: O(N log N) where N is the length of nums, dominated by sorting.
        // Space Complexity: O(1) auxiliary space if we modify the input array in place.
        // Explanation: Sorting the array allows us to easily access the minimum elements. 
        // In each round, Alice picks the smallest remaining (index i), and Bob picks the 
        // next smallest (index i + 1). When appending to arr, Bob goes first, then Alice, 
        // which effectively swaps every adjacent pair of elements in the sorted array.
        
        sort(nums.begin(), nums.end());
        
        // Swap adjacent pairs to simulate Bob appending before Alice
        for (size_t i = 0; i < nums.size(); i += 2) {
            swap(nums[i], nums[i + 1]);
        }
        
        return nums;
    }
};