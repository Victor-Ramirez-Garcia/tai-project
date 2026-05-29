#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    /**
     * The problem asks for the minimum seconds to fill all cups, where we can fill
     * 2 different types or 1 type per second. This is a variation of the load balancing 
     * or "triangular" inequality problem.
     * * Complexity Analysis:
     * Time Complexity: O(1) as the input size is constant (3).
     * Space Complexity: O(1).
     */
    int fillCups(vector<int>& amount) {
        // Sort to find the maximum element easily.
        sort(amount.begin(), amount.end());
        
        int a = amount[0];
        int b = amount[1];
        int c = amount[2];
        
        /* * Logic:
         * There are two primary cases:
         * 1. The largest pile (c) is greater than or equal to the sum of the other two (a + b).
         * In this case, we always pair one from c with one from either a or b until a and b 
         * are exhausted. The total time will simply be the size of the largest pile 'c'.
         * * 2. The largest pile (c) is less than the sum of the other two (a + b).
         * In this case, we can keep pairing different types until we have 0 or 1 cup left 
         * total (if total sum is even or odd). The minimum time is ceil(total_sum / 2).
         */
        
        int sum = a + b + c;
        
        // This math expression covers both cases:
        // Case 1: c >= a + b  =>  result is c
        // Case 2: c < a + b   =>  result is ceil(sum / 2.0)
        return max(c, (sum + 1) / 2);
    }
};