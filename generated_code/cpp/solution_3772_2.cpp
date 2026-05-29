#include <vector>
#include <queue>
#include <tuple>

using namespace std;

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        // Use long long to handle larger sums and prevent integer overflow
        vector<long long> vals(nums.begin(), nums.end());
        
        // Simulating a doubly-linked list via arrays to efficiently track active elements
        vector<int> nexts(n);
        vector<int> prevs(n);
        for (int i = 0; i < n; ++i) {
            nexts[i] = i + 1;
            prevs[i] = i - 1;
        }
        nexts[n - 1] = -1; // End marker

        // Min-heap to always retrieve the pair with the minimum sum. 
        // Elements are ordered by: (pair_sum, left_index).
        // Greater<tuple<...>> guarantees a min-heap structure, and lexicographical 
        // comparison naturally handles the leftmost element tie-breaker condition.
        priority_queue<tuple<long long, int>, vector<tuple<long long, int>>, greater<tuple<long long, int>>> pq;
        
        // Count how many adjacent pairs currently violate the non-decreasing order
        int unsorted_cnt = 0;
        for (int i = 0; i < n - 1; ++i) {
            pq.push({vals[i] + vals[i + 1], i});
            if (vals[i] > vals[i + 1]) {
                unsorted_cnt++;
            }
        }

        // Keep track of deleted elements to support lazy deletion from the priority queue
        vector<bool> removed(n, false);
        int moves = 0;

        // Process merges until the array becomes strictly non-decreasing
        while (unsorted_cnt > 0 && !pq.empty()) {
            auto [sum, u] = pq.top();
            pq.pop();

            // Lazy deletion: if the left element is already removed, skip it
            if (removed[u]) continue;

            int v = nexts[u];
            // Validate if the right neighbor exists, is not removed, and matches the recorded sum
            if (v == -1 || removed[v] || vals[u] + vals[v] != sum) continue;

            int p = prevs[u];
            int next_v = nexts[v];
            moves++;

            // Subtract old inversion pairs affected by the current merge operation
            if (p != -1 && vals[p] > vals[u]) unsorted_cnt--;
            if (vals[u] > vals[v]) unsorted_cnt--;
            if (next_v != -1 && vals[v] > vals[next_v]) unsorted_cnt--;

            // Perform the merge: accumulate value into the left element
            vals[u] += vals[v];
            removed[v] = true;

            // Re-link the simulated doubly-linked list
            nexts[u] = next_v;
            if (next_v != -1) {
                prevs[next_v] = u;
            }

            // Check new adjacent relationships for inversions and add new valid pairs to min-heap
            if (p != -1 && vals[p] > vals[u]) unsorted_cnt++;
            if (next_v != -1) {
                if (vals[u] > vals[next_v]) unsorted_cnt++;
                pq.push({vals[u] + vals[next_v], u});
            }
            if (p != -1) {
                pq.push({vals[p] + vals[u], p});
            }
        }

        return moves;
    }
};