#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int n = nums.size();
        
        // Find the next greater and next smaller elements to determine
        // the boundaries where each element acts as the maximum or minimum.
        vector<int> next_greater(n, n), prev_greater(n, -1);
        vector<int> next_smaller(n, n), prev_smaller(n, -1);
        
        stack<int> st;
        
        // Next Greater Element (using > to handle duplicates properly)
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && nums[st.top()] < nums[i]) {
                next_greater[st.top()] = i;
                st.pop();
            }
            if (!st.empty()) prev_greater[i] = st.top();
            st.push(i);
        }
        while (!st.empty()) st.pop();
        
        // Next Smaller Element (using < to handle duplicates properly)
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && nums[st.top()] > nums[i]) {
                next_smaller[st.top()] = i;
                st.pop();
            }
            if (!st.empty()) prev_smaller[i] = st.top();
            st.push(i);
        }
        
        // Max-heap to store the highest contributors to the total value.
        // Each entry is a pair: {contribution_value, subarray_count}
        priority_queue<long long> max_heap;
        
        // For each element, calculate how many subarrays it acts as the maximum
        // and how many it acts as the minimum, then push to the heap.
        for (int i = 0; i < n; ++i) {
            long long max_count = (long long)(i - prev_greater[i]) * (next_greater[i] - i);
            long long min_count = (long long)(i - prev_smaller[i]) * (next_smaller[i] - i);
            
            // Positive contribution when nums[i] is the maximum
            if (max_count > 0) {
                for (int j = 0; j < max_count && max_heap.size() < k; ++j) {
                    max_heap.push(nums[i]);
                }
            }
            // Negative contribution when nums[i] is the minimum
            if (min_count > 0) {
                for (int j = 0; j < min_count && max_heap.size() < k; ++j) {
                    max_heap.push(-nums[i]);
                }
            }
        }
        
        // Since we need the top k largest contributions globally across all subarrays:
        // We accumulate the largest positive components and subtract the smallest negative components.
        // Note: For a strict O((N + K) log K) or O(N log N) approach on large constraints,
        // we can sort all possible contributions. Given the problem type, we extract the top k.
        long long total_value = 0;
        
        // Generate sorted list of all individual max/min contributions
        vector<long long> all_maxs, all_mins;
        for (int i = 0; i < n; ++i) {
            long long max_count = (long long)(i - prev_greater[i]) * (next_greater[i] - i);
            long long min_count = (long long)(i - prev_smaller[i]) * (next_smaller[i] - i);
            for (int j = 0; j < max_count; ++j) all_maxs.push_back(nums[i]);
            for (int j = 0; j < min_count; ++j) all_mins.push_back(nums[i]);
        }
        
        sort(all_maxs.rbegin(), all_maxs.rend());
        sort(all_mins.begin(), all_mins.end());
        
        // The problem asks to pick exactly k distinct subarrays to maximize total value.
        // Each subarray's value is max - min. Sum of k subarrays = sum(k maxes) - sum(k mins).
        // To maximize this, we independently take the top k largest maximums and top k smallest minimums
        // because subarrays can be chosen flexibly (up to all N*(N+1)/2 subarrays).
        for (int i = 0; i < k && i < all_maxs.size(); ++i) {
            total_value += all_maxs[i];
        }
        for (int i = 0; i < k && i < all_mins.size(); ++i) {
            total_value -= all_mins[i];
        }
        
        return total_value;
    }
};