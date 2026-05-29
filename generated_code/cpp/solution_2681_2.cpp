#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        // If we need to divide into k bags, we need to make k - 1 splits.
        // Each split between index i and i+1 adds weights[i] + weights[i+1] to the total score.
        // The first element weights[0] and the last element weights[n-1] are always included
        // in both the minimum and maximum scores, so they cancel out in the difference.
        // Thus, the problem reduces to finding the sum of the k-1 largest pair sums 
        // minus the sum of the k-1 smallest pair sums.
        
        int n = weights.size();
        if (k == 1 || n == k) {
            return 0; // Only 1 way to distribute or 1 marble per bag, difference is 0.
        }
        
        vector<long long> pair_sums(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            pair_sums[i] = (long long)weights[i] + weights[i + 1];
        }
        
        // To find the sum of the k-1 smallest and largest elements efficiently, 
        // we can sort the pair sums. Time complexity: O(N log N).
        sort(pair_sums.begin(), pair_sums.end());
        
        long long min_score_components = 0;
        long long max_score_components = 0;
        
        // Sum the smallest k-1 pairs and the largest k-1 pairs.
        for (int i = 0; i < k - 1; ++i) {
            min_score_components += pair_sums[i];
            max_score_components += pair_sums[n - 2 - i];
        }
        
        return max_score_components - min_score_components;
    }
};