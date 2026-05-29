#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    int fillCups(vector<int>& amount) {
        // Find the maximum element in the amount array
        int max_val = *max_element(amount.begin(), amount.end());
        // Calculate the total sum of all elements
        int total_sum = accumulate(amount.begin(), amount.end(), 0);
        
        /* * Logic:
         * 1. If one type of water cup has a count greater than the sum of the other two, 
         * we can pair all of the other cups with this maximum type. The remaining cups 
         * of the maximum type must then be filled individually. Thus, the total time 
         * is bounded by max_val.
         * * 2. If the maximum element is less than or equal to the sum of the other two, 
         * we can always pair the cups optimally such that we fill 2 cups per second, 
         * leaving at most 1 cup left over if the total sum is odd. Thus, the total 
         * time is ceil(total_sum / 2.0), which is equivalent to (total_sum + 1) / 2.
         */
        return max(max_val, (total_sum + 1) / 2);
    }
};