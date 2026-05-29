#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        // Since we can only decrement elements, each decrement reduces the total sum by 1.
        // To make the sum divisible by k, we need to find the remainder of the total sum modulo k.
        // The minimum number of operations will be exactly equal to this remainder, 
        // as we can just decrement any element(s) to remove the remainder.
        
        long long total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }
        
        // Calculate the remainder. Since nums contains integers and we want to find 
        // the positive remainder (or 0) for the total sum relative to k:
        int remainder = total_sum % k;
        
        // Handle potential negative sum if constraints allowed negative numbers,
        // though standard array sum problems usually imply non-negative or require standard modulo math.
        if (remainder < 0) {
            remainder += k;
        }
        
        return remainder;
    }
};