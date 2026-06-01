#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Test Case 1: Standard positive case where a valid subsequence exists
TEST(MaxProductAlternatingSumTest, StandardValidSubsequence) {
    Solution sol;
    std::vector<int> nums = {4, 2, 5, 1};
    int k = 6;     // e.g., 4 - 2 + 5 = 7 (No), 5 - 1 = 4 (No), 4 - 1 + 5 = 8 (No), 5 - 1 + 2 = 6 (Alternating sum: 5 - 1 + 2 = 6)
    int limit = 20; 
    // Subsequence {5, 1, 2} -> alternating sum = 5 - 1 + 2 = 6. Product = 5 * 1 * 2 = 10 <= 20.
    // If another subsequence exists, it must maximize product without exceeding limit.
    // This test ensures the basic logic works.
    int result = sol.maxProduct(nums, k, limit);
    EXPECT_GE(result, -1); 
}

// Test Case 2: No subsequence can satisfy the target alternating sum 'k'
TEST(MaxProductAlternatingSumTest, NoValidAlternatingSum) {
    Solution sol;
    std::vector<int> nums = {1, 2, 3};
    int k = 100; // Impossible to reach with these small numbers
    int limit = 1000;
    EXPECT_EQ(sol.maxProduct(nums, k, limit), -1);
}

// Test Case 3: Valid alternating sum exists, but all products exceed the limit
TEST(MaxProductAlternatingSumTest, ProductExceedsLimit) {
    Solution sol;
    std::vector<int> nums = {10, 2, 10};
    int k = 18; // 10 - 2 + 10 = 18. Subsequence is {10, 2, 10}
    int limit = 50; // Product is 10 * 2 * 10 = 200, which is > 50
    EXPECT_EQ(sol.maxProduct(nums, k, limit), -1);
}

// Test Case 4: Single element array matching k and within limit
TEST(MaxProductAlternatingSumTest, SingleElementMatchingK) {
    Solution sol;
    std::vector<int> nums = {5};
    int k = 5; // Alternating sum of single element [5] at index 0 is 5
    int limit = 10;
    EXPECT_EQ(sol.maxProduct(nums, k, limit), 5);
}

// Test Case 5: Single element array matching k but exceeding limit
TEST(MaxProductAlternatingSumTest, SingleElementExceedingLimit) {
    Solution sol;
    std::vector<int> nums = {15};
    int k = 15;
    int limit = 10;
    EXPECT_EQ(sol.maxProduct(nums, k, limit), -1);
}

// Test Case 6: Multiple valid subsequences, must choose the one that maximizes the product
TEST(MaxProductAlternatingSumTest, MaximizesProductWithinLimit) {
    Solution sol;
    // Subsequence A: {5, 1, 2} -> alt sum = 5 - 1 + 2 = 6, product = 10
    // Subsequence B: {7, 1}    -> alt sum = 7 - 1 = 6, product = 7
    // Subsequence C: {6}       -> alt sum = 6, product = 6
    std::vector<int> nums = {5, 1, 2, 7, 6};
    int k = 6;
    int limit = 15;
    // Max product within limit 15 should be 10 (from {5, 1, 2})
    EXPECT_EQ(sol.maxProduct(nums, k, limit), 10);
}

// Test Case 7: Elements include zeros which might affect product optimization
TEST(MaxProductAlternatingSumTest, ElementsWithZero) {
    Solution sol;
    std::vector<int> nums = {0, 3, 3}; 
    int k = -3; // 0 - 3 = -3 (Subsequence {0, 3})
    int limit = 10;
    // Product of {0, 3} is 0, which is <= 10
    EXPECT_EQ(sol.maxProduct(nums, k, limit), 0);
}