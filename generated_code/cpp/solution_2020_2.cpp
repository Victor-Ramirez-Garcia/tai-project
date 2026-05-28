#include <vector>

using namespace std;

/**
 * Problem: 1909. Remove One Element to Make the Array Strictly Increasing
 * Approach: Single Pass Greedy Check
 * Time Complexity: O(n) - We iterate through the array once.
 * Space Complexity: O(1) - No extra space used except for variables.
 */
class Solution {
public:
    bool canBeIncreasing(vector<int>& nums) {
        int count = 0; // Tracks the number of elements we need to "remove"
        int n = nums.size();

        for (int i = 1; i < n; ++i) {
            // Check if there is a violation of the strictly increasing condition
            if (nums[i] <= nums[i - 1]) {
                count++;
                
                // If we've already found more than one violation, it's impossible
                if (count > 1) return false;

                /**
                 * When a violation occurs (nums[i] <= nums[i-1]), we have two choices:
                 * 1. Remove nums[i-1]: This is viable if nums[i] > nums[i-2].
                 * 2. Remove nums[i]: This is viable if nums[i+1] > nums[i-1] (handled by next iterations).
                 * * Logic:
                 * If i > 1 and the current element nums[i] is still smaller than or equal to 
                 * the element before the previous one (nums[i-2]), it means removing nums[i-1] 
                 * doesn't fix the sequence for nums[i]. Thus, we must "remove" nums[i] by 
                 * setting it to nums[i-1] to maintain the non-decreasing check for the next pair.
                 */
                if (i > 1 && nums[i] <= nums[i - 2]) {
                    nums[i] = nums[i - 1];
                }
            }
        }

        return count <= 1;
    }
};