#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        // Step 1: Sort the array in non-decreasing order.
        // This allows us to easily get the minimum elements in each round.
        // Time Complexity: O(N log N), where N is the length of nums.
        // Space Complexity: O(1) if sorting in place.
        sort(nums.begin(), nums.end());
        
        // Step 2: In every round, Alice removes the minimum (nums[i]) and 
        // Bob removes the next minimum (nums[i+1]).
        // Then Bob appends his element first, followed by Alice.
        // This is equivalent to swapping adjacent pairs in the sorted array.
        for (int i = 0; i < nums.size(); i += 2) {
            swap(nums[i], nums[i + 1]);
        }
        
        return nums;
    }
};