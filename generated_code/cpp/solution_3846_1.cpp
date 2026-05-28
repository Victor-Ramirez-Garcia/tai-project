#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        // The operation allows us to decrement any element by 1.
        // To make the total sum divisible by k, we need the sum of the array 
        // modulo k to be 0. 
        // 
        // Let S be the current sum of the array. We want to find the minimum 
        // number of subtractions to reach a sum S' such that S' % k == 0 and S' <= S.
        // The closest multiple of k that is less than or equal to S is S - (S % k).
        // Therefore, the minimum number of operations required is exactly S % k.
        //
        // Time Complexity: O(N) to sum the array elements.
        // Space Complexity: O(1) auxiliary space.
        
        long long total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }
        
        return total_sum % k;
    }
};