#include <vector>
#include <queue>
#include <tuple>

using namespace std;

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        // Custom comparator for the min-heap.
        // It prefers smaller sums first, and then smaller left indices for tie-breaking.
        auto cmp = [](const tuple<long long, int, int>& a, const tuple<long long, int, int>& b) {
            if (get<0>(a) != get<0>(b)) {
                return get<0>(a) > get<0>(b);
            }
            return get<1>(a) > get<1>(b);
        };

        // Priority queue elements: {pair_sum, left_index, unique_id_of_left_index}
        priority_queue<tuple<long long, int, int>, vector<tuple<long long, int, int>>, decltype(cmp)> pq(cmp);

        // Doubly linked list representations to track active adjacencies.
        vector<int> left_neighbor(n);
        vector<int> right_neighbor(n);
        // Version tracker for each index to handle lazy deletion in the min-heap efficiently.
        vector<int> version(n, 0);

        // Count of active adjacent pairs where elements are strictly decreasing.
        int decreasing_count = 0;

        // Initialize structures
        for (int i = 0; i < n; ++i) {
            left_neighbor[i] = i - 1;
            right_neighbor[i] = i + 1;
            if (i < n - 1) {
                pq.push({(long long)nums[i] + nums[i + 1], i, 0});
                if (nums[i] > nums[i + 1]) {
                    decreasing_count++;
                }
            }
        }

        int operations = 0;

        // Simulate the operation as long as the array is not non-decreasing
        while (decreasing_count > 0 && !pq.empty()) {
            auto [current_sum, i, v] = pq.top();
            pq.pop();

            // Lazy deletion check: verify if the pair metadata matches its current state.
            if (v != version[i] || right_neighbor[i] >= n) {
                continue;
            }

            int j = right_neighbor[i];

            // Safely decrement decreasing counts for the pairs being disrupted
            if (nums[i] > nums[j]) decreasing_count--;
            if (left_neighbor[i] >= 0 && nums[left_neighbor[i]] > nums[i]) decreasing_count--;
            if (right_neighbor[j] < n && nums[j] > nums[right_neighbor[j]]) decreasing_count--;

            // Perform the substitution: replace pair with their sum
            long long new_val = (long long)nums[i] + nums[j];
            // Clip value within safe integer boundaries to prevent extreme under/overflow issues
            if (new_val > 2e9) new_val = 2e9;
            if (new_val < -2e9) new_val = -2e9;
            nums[i] = static_cast<int>(new_val);

            // Update doubly linked list topology to erase index `j`
            right_neighbor[i] = right_neighbor[j];
            if (right_neighbor[j] < n) {
                left_neighbor[right_neighbor[j]] = i;
            }

            // Invalidate existing heap references to index `i` by incrementing its version
            version[i]++;
            operations++;

            // Re-evaluate and increment decreasing counts based on new neighbor relationships
            if (left_neighbor[i] >= 0 && nums[left_neighbor[i]] > nums[i]) decreasing_count++;
            if (right_neighbor[i] < n && nums[i] > nums[right_neighbor[i]]) decreasing_count++;

            // Push the updated adjacent pair back into the min-heap
            if (right_neighbor[i] < n) {
                pq.push({(long long)nums[i] + nums[right_neighbor[i]], i, version[i]});
            }
        }

        return operations;
    }
};