#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        // Algorithmic Choice: Greedy / Sorting
        // Time Complexity: O(N log N) where N is the number of elements in weights, due to sorting.
        // Space Complexity: O(N) to store the adjacent pair weights.
        
        int n = weights.size();
        
        // If the number of bags equals the number of elements, or there's only 1 bag, 
        // the max and min scores will be identical, so the difference is 0.
        if (k == 1 || k == n) {
            return 0;
        }
        
        // When we split the array into k subarrays, we make exactly k - 1 splits.
        // A split between index i and i + 1 adds weights[i] + weights[i+1] to the score.
        // The first element weights[0] and the last element weights[n-1] are always included in the score.
        // Thus, the total score variation depends entirely on the sum of the chosen k - 1 adjacent pairs.
        vector<long long> pairWeights;
        pairWeights.reserve(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            pairWeights.push_back((long long)weights[i] + weights[i + 1]);
        }
        
        // Sort the pairs to easily pick the smallest and largest ones.
        sort(pairWeights.begin(), pairWeights.end());
        
        long long minScoreSubsum = 0;
        long long maxScoreSubsum = 0;
        
        // To minimize the score, choose the k - 1 smallest pairs.
        // To maximize the score, choose the k - 1 largest pairs.
        for (int i = 0; i < k - 1; ++i) {
            minScoreSubsum += pairWeights[i];
            maxScoreSubsum += pairWeights[pairWeights.size() - 1 - i];
        }
        
        // The constant terms weights[0] and weights[n-1] cancel out in the difference.
        return maxScoreSubsum - minScoreSubsum;
    }
};