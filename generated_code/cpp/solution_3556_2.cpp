#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
private:
    // Helper function for modular exponentiation: (base^exp) % mod
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
        // Edge case: if multiplier is 1, elements never change magnitude.
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

        // Custom comparator for min-heap: 
        // 1. Prioritize smaller values.
        // 2. Prioritize smaller indices if values are equal.
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

        // Phase 1: Simulate using min-heap until the minimum element 
        // becomes >= the original maximum element, or we run out of k operations.
        while (k > 0 && pq.top().first * multiplier <= max_val * multiplier) {
            auto [val, idx] = pq.top();
            pq.pop();
            pq.push({val * multiplier, idx});
            k--;
        }

        // If elements haven't stabilized but k became 0, we can just extract from heap.
        if (k == 0) {
            vector<int> res(n);
            while (!pq.empty()) {
                auto [val, idx] = pq.top();
                pq.pop();
                res[idx] = val % MOD;
            }
            return res;
        }

        // Phase 2: All elements are balanced in a cycle.
        // We sort the remaining elements based on their current values and indices.
        vector<pair<long long, int>> elements;
        while (!pq.empty()) {
            elements.push_back(pq.top());
            pq.pop();
        }
        // Re-sorting ensures we strictly match the order of operation choice
        sort(elements.begin(), elements.end(), [](const pair<long long, int>& a, const pair<long long, int>& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second < b.second;
        });

        // Each element gets at least (k / n) full cycles of multiplication
        long long base_pow = k / n;
        int remaining_ops = k % n;

        long long mult_base = power(multiplier, base_pow, MOD);
        long long mult_extra = (mult_base * multiplier) % MOD;

        vector<int> res(n);
        for (int i = 0; i < n; ++i) {
            long long val = elements[i].first % MOD;
            int idx = elements[i].second;
            
            // The first `remaining_ops` elements in the sorted list get 1 extra multiplication
            if (i < remaining_ops) {
                res[idx] = (val * mult_extra) % MOD;
            } else {
                res[idx] = (val * mult_base) % MOD;
            }
        }

        return res;
    }
};