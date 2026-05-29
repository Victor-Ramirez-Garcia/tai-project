#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
private:
    const int MOD = 1e9 + 7;

    // Helper function for modular exponentiation: (base^exp) % MOD
    long long power(long long base, long long exp) {
        long long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }

public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        // Edge case: if multiplier is 1, array elements never change value
        if (multiplier == 1) {
            vector<int> res(nums.size());
            for (size_t i = 0; i < nums.size(); ++i) {
                res[i] = nums[i] % MOD;
            }
            return res;
        }

        int n = nums.size();
        // Min-heap to track {value, original_index}. 
        // Pairs are compared by value first, then by index to handle duplicates correctly.
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        
        long long max_val = 0;
        for (int i = 0; i < n; ++i) {
            pq.push({nums[i], i});
            max_val = max(max_val, (long long)nums[i]);
        }

        // Phase 1: Simulate operations greedily until the minimum element 
        // multiplied by the multiplier exceeds the initial maximum element.
        // This brings all elements to a state where they are roughly balanced.
        while (k > 0 && pq.top().first * multiplier <= max_val) {
            auto [val, idx] = pq.top();
            pq.pop();
            pq.push({val * multiplier, idx});
            k--;
        }

        // Phase 2: Once the array is balanced, additional cycles of operations 
        // will multiply each element by `multiplier` in a predictable, uniform way.
        int full_cycles = k / n;
        int remaining_ops = k % n;

        // Precompute multiplier factors using modular exponentiation
        long long factor_full = power(multiplier, full_cycles);
        long long factor_extra = power(multiplier, full_cycles + 1);

        vector<int> result(n);
        
        // The first `remaining_ops` elements extracted from the heap will get 
        // an extra multiplication since they are the smallest elements in the current state.
        for (int i = 0; i < n; ++i) {
            auto [val, idx] = pq.top();
            pq.pop();
            
            long long current_factor = (i < remaining_ops) ? factor_extra : factor_full;
            result[idx] = ((val % MOD) * current_factor) % MOD;
        }

        return result;
    }
};