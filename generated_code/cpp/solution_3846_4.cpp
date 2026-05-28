#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        // The operation allows us to decrement any element by 1.
        // To make the sum divisible by k, we want the final sum to be a multiple of k.
        // Since we can only decrease elements, the total sum can only decrease.
        // To minimize the number of operations, we want to find the smallest non-negative 
        // reduction needed to make the total sum divisible by k.
        // This is exactly equivalent to total_sum % k.
        
        long long total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }
        
        // Return the remainder when total_sum is divided by k.
        // This represents the minimum operations required (each operation reduces the sum by 1).
        return total_sum % k;
    }
};