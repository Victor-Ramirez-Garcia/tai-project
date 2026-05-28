#include <vector>

using namespace std;

class Solution {
public:
    bool canBeIncreasing(vector<int>& nums) {
        int count = 0; // Tracks the number of violations where nums[i-1] >= nums[i]
        int n = nums.size();
        
        for (int i = 1; i < n; ++i) {
            if (nums[i - 1] >= nums[i]) {
                count++;
                // If more than one element needs to be removed, it's impossible
                if (count > 1) {
                    return false;
                }
                
                // Determine which element to "remove" (i-1 or i) to maintain the strictly increasing property.
                // We check if removing nums[i-1] fixes the violation.
                // If i == 1, removing nums[0] always works.
                // If nums[i-2] < nums[i], removing nums[i-1] works, so we conceptually keep nums[i].
                // Otherwise, we must remove nums[i]. To simulate this, we modify nums[i] to be nums[i-1].
                if (i > 1 && nums[i - 2] >= nums[i]) {
                    nums[i] = nums[i - 1];
                }
            }
        }
        
        return true;
    }
};