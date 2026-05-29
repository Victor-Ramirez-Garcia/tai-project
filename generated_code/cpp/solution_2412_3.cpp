#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    /**
     * Problem: Minimum Amount of Time to Fill Cups
     * Strategy: Greedy / Math
     * * We have two scenarios:
     * 1. One type of water is so frequent that it is greater than or equal to the sum 
     * of the other two. In this case, we can pair all of the smaller two types 
     * with the largest type, and the total time is simply the max(amount).
     * * 2. The amounts are relatively balanced. In this case, we can always pair 
     * different types until at most 1 cup remains. The total time becomes 
     * ceil(sum(amount) / 2).
     * * Time Complexity: O(1) as the input size is constant (3).
     * Space Complexity: O(1).
     */
    int fillCups(vector<int>& amount) {
        int max_val = 0;
        int sum_val = 0;
        
        for (int x : amount) {
            max_val = max(max_val, x);
            sum_val += x;
        }
        
        // If the largest element is greater than the sum of the others, 
        // the bottleneck is the largest element itself.
        // Otherwise, we can pair elements efficiently to reach ceil(sum/2).
        return max(max_val, (sum_val + 1) / 2);
    }
};