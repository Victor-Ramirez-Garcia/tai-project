#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        // Algorithm: Sorting and Swapping adjacent pairs.
        // Time Complexity: O(N log N) due to sorting, where N is the number of elements.
        // Space Complexity: O(1) auxiliary space as we modify the array in-place.
        
        // Sorting allows us to easily find the minimum elements in each round.
        // In any pair of the sorted array, nums[i] is Alice's choice (smaller) 
        // and nums[i+1] is Bob's choice (larger).
        sort(nums.begin(), nums.end());
        
        // Since Bob appends his element first and Alice appends hers second,
        // we swap every adjacent pair to match the required output order.
        for (size_t i = 0; i < nums.size(); i += 2) {
            swap(nums[i], nums[i + 1]);
        }
        
        return nums;
    }
};