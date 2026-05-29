#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        // Core Idea: Splitting the array into k bags requires choosing k - 1 partition points.
        // If we split between index i and i + 1, the right boundary of the current bag is weights[i]
        // and the left boundary of the next bag is weights[i + 1]. Thus, every split contributes 
        // weights[i] + weights[i + 1] to the total score. 
        // The first element weights[0] and the last element weights[n - 1] are always part of the 
        // score regardless of how we split.
        // Therefore, finding the max/min total score is equivalent to finding the sum of the 
        // largest/smallest k - 1 adjacent pair sums.

        int n = weights.size();
        if (k == 1 || n == k) {
            return 0; // Only one valid distribution, so max_score - min_score = 0
        }

        // Generate all possible adjacent pair sums
        vector<long long> pair_sums(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            pair_sums[i] = static_cast<long long>(weights[i]) + weights[i + 1];
        }

        // To optimize, we don't need a full sort. We can use std::nth_element 
        // to find the smallest and largest k - 1 elements in O(N) time.
        int num_splits = k - 1;

        // Find the sum of the smallest k - 1 elements
        nth_element(pair_sums.begin(), pair_sums.begin() + num_splits, pair_sums.end());
        long long min_splits_sum = 0;
        for (int i = 0; i < num_splits; ++i) {
            min_splits_sum += pair_sums[i];
        }

        // Find the sum of the largest k - 1 elements
        nth_element(pair_sums.begin(), pair_sums.begin() + (n - 1 - num_splits), pair_sums.end());
        long long max_splits_sum = 0;
        for (int i = n - 1 - num_splits; i < n - 1; ++i) {
            max_splits_sum += pair_sums[i];
        }

        // The difference in total scores is exactly the difference between the partition choices,
        // because weights[0] and weights[n - 1] cancel out.
        return max_splits_sum - min_splits_sum;
    }
};