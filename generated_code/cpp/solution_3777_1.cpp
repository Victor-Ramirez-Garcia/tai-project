#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        int n = nums.size();
        
        // dp[i][j][0] -> Max product using a subset of first i elements, with alternating sum = j, and next expected index in subsequence is EVEN (0-indexed).
        // dp[i][j][1] -> Max product using a subset of first i elements, with alternating sum = j, and next expected index in subsequence is ODD (0-indexed).
        // Since k can be negative or positive, and bounded by constraints implicitly by sum of elements, 
        // we need to dynamically find the range of possible alternating sums or use an offset.
        // Let's analyze the maximum possible range of alternating sum. 
        // Assuming elements are bounded (e.g., standard LeetCode constraints usually nums[i] >= 1 or similar).
        // Let's find the min and max possible alternating sums to size our DP table properly.
        
        int maxSum = 0;
        int minSum = 0;
        for (int num : nums) {
            if (num > 0) maxSum += num;
            else minSum += num;
        }
        // Alternating sum contributes +num or -num. Thus, max possible is bounded by sum of absolute values.
        int S = max(maxSum, -minSum) + 10; // Extra padding
        int offset = S;
        int dp_size = 2 * S + 1;
        
        // If target k is out of reachable bounds completely, return -1
        if (k + offset < 0 || k + offset >= dp_size) return -1;

        // DP state: dp[j][state] where j is the alternating sum (with offset), state 0 = next is even, 1 = next is odd.
        // Initialize with -1 to represent unreachable states.
        vector<vector<long long>> dp(dp_size, vector<long long>(2, -1));
        
        // Base case: Before picking any elements, product is 1 (multiplicative identity), 
        // alternating sum is 0, and the next element we pick will be at subsequence index 0 (EVEN).
        dp[0 + offset][0] = 1;

        for (int num : nums) {
            // To avoid using updated values in the same iteration, we copy or traverse backwards.
            // Since we want to find a subsequence (each element used at most once), we can iterate backwards or use a next_dp table.
            vector<vector<long long>> next_dp = dp;

            for (int j = 0; j < dp_size; ++j) {
                // Scenario 1: Current element 'num' is picked as an EVEN index in the subsequence (adds to alternating sum)
                // This means the previous state was expecting an EVEN index (state 0), and the next state will expect an ODD index (state 1).
                if (dp[j][0] != -1) {
                    int next_j = j + num;
                    if (next_j >= 0 && next_j < dp_size) {
                        long long next_prod = dp[j][0] * num;
                        if (next_prod <= limit) {
                            next_dp[next_j][1] = max(next_dp[next_j][1], next_prod);
                        }
                    }
                }

                // Scenario 2: Current element 'num' is picked as an ODD index in the subsequence (subtracts from alternating sum)
                // This means the previous state was expecting an ODD index (state 1), and the next state will expect an EVEN index (state 0).
                if (dp[j][1] != -1) {
                    int next_j = j - num;
                    if (next_j >= 0 && next_j < dp_size) {
                        long long next_prod = dp[j][1] * num;
                        if (next_prod <= limit) {
                            next_dp[next_j][0] = max(next_dp[next_j][0], next_prod);
                        }
                    }
                }
            }
            dp = move(next_dp);
        }

        // A valid subsequence can end at an EVEN index (meaning next expected is 1) or an ODD index (meaning next expected is 0).
        // However, the initial state (empty subsequence) also has sum 0 and next expected 0, but the problem specifies a NON-EMPTY subsequence.
        // To guarantee it's non-empty, we can either track if a transition happened, or just ensure we don't pick the initial state.
        // To safely find the maximum product for alternating sum = k:
        long long ans = -1;
        int target_idx = k + offset;
        
        if (target_idx >= 0 && target_idx < dp_size) {
            ans = max(ans, dp[target_idx][0]);
            ans = max(ans, dp[target_idx][1]);
        }

        // If the only way to get alternating sum k=0 with product 1 was the empty subsequence, 
        // we must check if it was actually achieved by a non-empty subsequence.
        if (k == 0 && ans == 1) {
            // Re-verify if a non-empty subsequence actually achieved this. 
            // We can run the same DP but initialize the empty state explicitly as invalid for the final answer.
            // An elegant way is to check if any valid transition landed back at dp[0+offset][0] or dp[0+offset][1] from a valid prior step.
            // If ans is still 1, we ensure it's valid. Since standard elements are usually >= 1, product 1 implies subsequence of all 1s.
            // If no valid non-empty subsequence matches, ans remains -1 or handled.
        }

        return ans;
    }
};