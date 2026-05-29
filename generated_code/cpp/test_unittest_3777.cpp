#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

// Test case 1: Base case where a single element matches k and is within limit
TEST(MaxProductAlternatingSumTest, SingleElementExactMatch) {
    Solution sol;
    vector<int> nums = {5};
    int k = 5;
    int limit = 10;
    // Subsequence [5] has alternating sum = 5 == k. Product = 5 <= limit.
    EXPECT_EQ(sol.maxProduct(nums, k, limit), 5);
}

// Test case 2: Element matches k but exceeds the limit
TEST(MaxProductAlternatingSumTest, SingleElementExceedsLimit) {
    Solution sol;
    vector<int> nums = {15};
    int k = 15;
    int limit = 10;
    // Subsequence [15] matches k but product 15 > limit. No other subsequences.
    EXPECT_EQ(sol.maxProduct(nums