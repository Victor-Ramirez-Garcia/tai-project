#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        // Algorithm: Math / Remainder Greedy approach
        // Time Complexity: O(N) where N is the number of elements in nums
        // Space Complexity: O(1) auxiliary space
        
        long long totalOperations = 0;
        
        for (int num : nums) {
            // Since we can only decrement elements (nums[i] = nums[i] - 1),
            // the operation reduces the value and consequently reduces its remainder modulo k.
            // For each number, to contribute to making the overall sum divisible by k,
            // we can greedily reduce it until its remainder becomes 0.
            // The number of operations to make a single positive number's remainder 0 
            // by decrementing is exactly (num % k).
            // If num % k is already 0, 0 operations are needed.
            
            int remainder = num % k;
            if (remainder < 0) {
                // Handle negative numbers if applicable based on standard C++ modulo behavior
                remainder += k;
            }
            
            totalOperations += remainder;
        }
        
        return totalOperations;
    }
};