#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canBeIncreasing(vector<int>& nums) {
        int count = 0; // Tracks the number of violations found
        int n = nums.size();
        
        for (int i = 1; i < n; ++i) {
            // Check if there is a violation of the strictly increasing property
            if (nums[i - 1] >= nums[i]) {
                count++;
                // If more than one violation is found, we cannot make it strictly increasing by removing just one element
                if (count > 1) {
                    return false;
                }
                
                // We have two choices to fix the violation:
                // 1. Remove nums[i - 1]: This is valid if nums[i - 2] < nums[i]
                // 2. Remove nums[i]: This is valid if nums[i - 1] < nums[i + 1]
                // If we are at the second element (i == 1), removing nums[i - 1] is always valid.
                // If neither option works to maintain the increasing order, we must modify the current state 
                // as if we "removed" nums[i] to prevent future false positives.
                if (i > 1 && nums[i - 2] >= nums[i]) {
                    // Simulating the removal of nums[i] by carrying forward the larger element nums[i - 1]
                    nums[i] = nums[i - 1];
                }
            }
        }
        
        return true;
    }
};