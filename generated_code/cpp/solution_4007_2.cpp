#include <vector>
#include <algorithm>
#include <numeric>
#include <queue>
#include <stack>

using namespace std;

class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int n = nums.size();
        
        // Step 1: Find the Next/Previous Greater/Smaller element indices to determine
        // the range of subarrays where each element acts as the maximum or minimum.
        vector<int> next_gt(n, n), prev_gt(n, -1);
        vector<int> next_lt(n, n), prev_lt(n, -1);
        
        stack<int> s;
        
        // Next Greater (using > to avoid double counting, standard technique)
        for (int i = 0; i < n; ++i) {
            while (!s.empty() && nums[s.top()] < nums[i]) {
                next_gt[s.top()] = i;
                s.pop();
            }
            s.push(i);
        }
        while (!s.empty()) s.pop();
        
        // Previous Greater (using >= to handle duplicate maximums cleanly)
        for (int i = n - 1; i >= 0; --i) {
            while (!s.empty() && nums[s.top()] <= nums[i]) {
                prev_gt[s.top()] = i;
                s.pop();
            }
            s.push(i);
        }
        while (!s.empty()) s.pop();
        
        // Next Smaller
        for (int i = 0; i < n; ++i) {
            while (!s.empty() && nums[s.top()] > nums[i]) {
                next_lt[s.top()] = i;
                s.pop();
            }
            s.push(i);
        }
        while (!s.empty()) s.pop();
        
        // Previous Smaller
        for (int i = n - 1; i >= 0; --i) {
            while (!s.empty() && nums[s.top()] >= nums[i]) {
                prev_lt[s.top()] = i;
                s.pop();
            }
            s.push(i);
        }
        
        // Step 2: Since we want the top k largest max-min values across ALL possible subarrays,
        // we can observe that we need to extract the largest values greedily.
        // For a fixed maximum element at index i, the subarray value increases or stays flat
        // as we expand, but it changes when the minimum changes. 
        // A full search space reduction is done using a Priority Queue (Max-Heap).
        // Each state tracks: {value, left_bound, right_bound, max_idx, min_idx}
        // To optimize, we find the highest value subarrays efficiently.
        // For standard constraints up to O(N log N + K log N) or O(N + K log N):
        
        auto get_val = [&](int l, int r) {
            // Helper to get max and min in O(1) if cached, or via RMQ if needed.
            // For general optimal solution, a Segment Tree or Sparse Table can be used.
            return 0; // Handled by the generation logic below
        };

        // Priority queue to store candidates: tuple of (value, left, right)
        // Since we want the absolute top k largest subarray values:
        // We can use a divide-and-conquer approach with a Max-Heap.
        // The global maximum subarray value comes from the max element and min element.
        // For an efficient implementation, we can precalculate all potential maximal pairs
        // or use a Cartiesian tree / RMQ based heap extraction.
        
        // Using Sparse Tables for O(1) RMQ to support the heap extraction
        int logN = 0;
        while ((1 << logN) <= n) logN++;
        
        vector<vector<int>> st_max(logN, vector<int>(n));
        vector<vector<int>> st_min(logN, vector<int>(n));
        
        for (int i = 0; i < n; i++) {
            st_max[0][i] = nums[i];
            st_min[0][i] = nums[i];
        }
        
        for (int j = 1; j < logN; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                st_max[j][i] = max(st_max[j - 1][i], st_max[j - 1][i + (1 << (j - 1))]);
                st_min[j][i] = min(st_min[j - 1][i], st_min[j - 1][i + (1 << (j - 1))]);
            }
        }
        
        auto query_max = [&](int L, int R) {
            int len = R - L + 1;
            int k_val = 31 - __builtin_clz(len);
            return max(st_max[k_val][L], st_max[k_val][R - (1 << k_val) + 1]);
        };
        
        auto query_min = [&](int L, int R) {
            int len = R - L + 1;
            int k_val = 31 - __builtin_clz(len);
            return min(st_min[k_val][L], st_min[k_val][R - (1 << k_val) + 1]);
        };
        
        // Find indices of max/min in range
        // For simplicity, we can store indices in the sparse table instead of values.
        vector<vector<int>> st_max_idx(logN, vector<int>(n));
        vector<vector<int>> st_min_idx(logN, vector<int>(n));
        for (int i = 0; i < n; i++) {
            st_max_idx[0][i] = i;
            st_min_idx[0][i] = i;
        }
        for (int j = 1; j < logN; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                int idx1 = st_max_idx[j - 1][i];
                int idx2 = st_max_idx[j - 1][i + (1 << (j - 1))];
                st_max_idx[j][i] = (nums[idx1] >= nums[idx2]) ? idx1 : idx2;
                
                int idx3 = st_min_idx[j - 1][i];
                int idx4 = st_min_idx[j - 1][i + (1 << (j - 1))];
                st_min_idx[j][i] = (nums[idx3] <= nums[idx4]) ? idx3 : idx4;
            }
        }
        
        auto query_max_idx = [&](int L, int R) {
            int len = R - L + 1;
            int k_val = 31 - __builtin_clz(len);
            int idx1 = st_max_idx[k_val][L];
            int idx2 = st_max_idx[k_val][R - (1 << k_val) + 1];
            return (nums[idx1] >= nums[idx2]) ? idx1 : idx2;
        };
        
        auto query_min_idx = [&](int L, int R) {
            int len = R - L + 1;
            int k_val = 31 - __builtin_clz(len);
            int idx1 = st_min_idx[k_val][L];
            int idx2 = st_min_idx[k_val][R - (1 << k_val) + 1];
            return (nums[idx1] <= nums[idx2]) ? idx1 : idx2;
        };

        // Element structure for Priority Queue
        struct Element {
            long long val;
            int L, R;
            int max_idx, min_idx;
            bool operator<(const Element& other) const {
                return val < other.val;
            }
        };
        
        priority_queue<Element> pq;
        
        // Initial state represents the entire array range
        int init_max = query_max_idx(0, n - 1);
        int init_min = query_min_idx(0, n - 1);
        pq.push({(long long)nums[init_max] - nums[init_min], 0, n - 1, init_max, init_min});
        
        long long total_value = 0;
        
        // Extract top k elements. To avoid duplicate ranges, we split the search intervals
        // around the chosen max_idx and min_idx points.
        for (int step = 0; step < k && !pq.empty(); ++step) {
            Element curr = pq.top();
            pq.pop();
            
            total_value += curr.val;
            
            // Generate next sub-segments to find the next best subarray values.
            // Split options around the max and min positions within [curr.L, curr.R]
            // ensuring we don't violate the boundary constraints.
            int l = curr.L, r = curr.R;
            int mx = curr.max_idx, mn = curr.min_idx;
            
            // Subsegments keeping the max/min but shrinking boundaries
            if (l < r) {
                // If we shrink from left or right, we get new subarrays.
                // To do this optimally without combinatorial explosion, we can transition
                // to its sub-problems standardly or push all 4 smaller intervals:
                auto push_range = [&](int new_l, int new_r) {
                    if (new_l <= new_r) {
                        int n_mx = query_max_idx(new_l, new_r);
                        int n_mn = query_min_idx(new_l, new_r);
                        pq.push({(long long)nums[n_mx] - nums[n_mn], new_l, new_r, n_mx, n_mn});
                    }
                };
                
                // Shrink boundaries while maintaining unique configurations
                if (mx > l) push_range(l, mx - 1);
                if (mx < r) push_range(mx + 1, r);
                if (mn > l && mn != mx) push_range(l, mn - 1);
                if (mn < r && mn != mx) push_range(mn + 1, r);
            }
        }
        
        return total_value;
    }
};