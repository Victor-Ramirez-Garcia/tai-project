#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

// Test Case 1: Covering the provided example scenario
TEST(MaxTotalValueTest, ExampleCase) {
    Solution sol;
    vector<int> nums = {1, 3, 2};
    int k = 2;
    // Subarrays chosen: nums[0..1] -> [1, 3] (val: 3-1=2) and nums[0..2] -> [1, 3, 2] (val: 3-1=2)
    // Total value = 2 + 2 = 4
    long long expected = 4;
    EXPECT_EQ(sol.maxTotalValue(nums, k), expected);
}

// Test Case 2: Minimal array size and minimum k
TEST(MaxTotalValueTest, MinimalInputEdgeCase) {
    Solution sol;
    vector<int> nums = {5};
    int k = 1;
    // Only one possible subarray: [5]. Value: 5 - 5 = 0
    long long expected = 0;
    EXPECT_EQ(sol.maxTotalValue(nums, k), expected);
}

// Test Case 3: All elements are identical
TEST(MaxTotalValueTest, IdenticalElements) {
    Solution sol;
    vector<int> nums = {7, 7, 7, 7};
    int k = 3;
    // Any subarray will have max == min, so value is always 0
    long long expected = 0;
    EXPECT_EQ(sol.maxTotalValue(nums, k), expected);
}

// Test Case 4: Strictly increasing array
TEST(MaxTotalValueTest, StrictlyIncreasingArray) {
    Solution sol;
    vector<int> nums = {1, 2, 4, 7};
    int k = 3;
    // Potential subarrays and their values:
    // [1, 2, 4, 7] -> 7 - 1 = 6
    // [2, 4, 7]    -> 7 - 2 = 5
    // [1, 2, 4]    -> 4 - 1 = 3
    // [4, 7]       -> 7 - 4 = 3
    // Top 3 distinct subarrays with max values would be 6 + 5 + 3 = 14 (or 6 + 5 + 3 from another combination)
    long long expected = 14;
    EXPECT_EQ(sol.maxTotalValue(nums, k), expected);
}

// Test Case 5: Large values that could cause 32-bit integer overflow in total sum
TEST(MaxTotalValueTest, PotentialOverflowHandling) {
    Solution sol;
    vector<int> nums = {-1000000000, 1000000000, 1000000000, -1000000000};
    int k = 2;
    // Subarray 1: [ -1e9, 1e9 ] -> 1e9 - (-1e9) = 2,000,000,000
    // Subarray 2: [ 1e9, 1e9, -1e9 ] -> 1e9 - (-1e9) = 2,000,000,000
    // Total = 4,000,000,000 (Exceeds standard signed 32-bit int max of ~2.14x10^9)
    long long expected = 4000000000LL;
    EXPECT_EQ(sol.maxTotalValue(nums, k), expected);
}

// Test Case 6: Maxing out k to choose all possible subarrays
TEST(MaxTotalValueTest, SelectAllSubarrays) {
    Solution sol;
    vector<int> nums = {1, 5, 2};
    // Total non-empty subarrays for size 3 is n*(n+1)/2 = 6
    // Subarrays and values:
    // [1] -> 0, [5] -> 0, [2] -> 0
    // [1, 5] -> 4
    // [5, 2] -> 3
    // [1, 5, 2] -> 4
    // Total sum = 0 + 0 + 0 + 4 + 3 + 4 = 11
    int k = 6;
    long long expected = 11;
    EXPECT_EQ(sol.maxTotalValue(nums, k), expected);
}