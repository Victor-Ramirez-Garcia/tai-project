#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
private:
    // Helper function for fast modular exponentiation: (base^exp) % mod
    long long power(long long base, long long exp, long long mod) {
        long long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }

public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        // Edge case: if multiplier is 1, array elements never change value
        if (multiplier == 1) {
            long long MOD = 1e9 + 7;
            vector<int> res(nums.size());
            for (int i = 0; i < nums.size(); ++i) {
                res[i] = nums[i] % MOD;
            }
            return res;
        }

        int n = nums.size();
        long long MOD = 1e9 + 7;

        // Min-heap stores pairs of {current_value, original_index}
        // Custom comparator ensures that if values are equal, the smaller index comes first
        auto comp = [](const pair<long long, int>& a, const pair<long long, int>& b) {
            if (a.first != b.first) return a.first > b.first;
            return a.second > b.second;
        };
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, decltype(comp)> pq(comp);

        long long max_val = 0;
        for (int i = 0; i < n; ++i) {
            pq.push({nums[i], i});
            max_val = max(max_val, (long long)nums[i]);
        }

        // Phase 1: Simulation until the minimum element can reach or exceed the initial maximum.
        // This ensures all elements become relatively close in magnitude, establishing a cyclical order.
        while (k > 0 && pq.top().first * multiplier <= max_val * multiplier) {
            auto [val, idx] = pq.top();
            pq.pop();
            pq.push({val * multiplier, idx});
            k--;
        }

        // Phase 2: Mass processing using mathematical cycles.
        // Collect all elements from the heap into a sorted list based on their current states.
        vector<pair<long long, int>> sorted_elements;
        while (!pq.empty()) {
            sorted_elements.push_back(pq.top());
            pq.pop();
        }
        // Since pq is already a min-heap, popping all elements gives them in the exact order they will be picked.
        reverse(sorted_elements.begin(), sorted_elements.end()); 

        // Each element will get at least (k / n) complete cycles of multiplications.
        long long base_power = k / n;
        int remaining_ops = k % n;

        vector<int> final_state(n);
        for (int i = 0; i < n; ++i) {
            long long val = sorted_elements[i].first;
            int idx = sorted_elements[i].second;

            // The first 'remaining_ops' elements in the cycle get one extra multiplication.
            long long total_mults = base_power + (i < remaining_ops ? 1 : 0);

            long long mult_factor = power(multiplier, total_mults, MOD);
            final_state[idx] = ((val % MOD) * mult_factor) % MOD;
        }

        return final_state;
    }
};