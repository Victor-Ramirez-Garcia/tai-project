#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Test Case 1: Standard example where a valid pair exists with no overlapping bits.
// e.g., nums = [3, 4, 8, 12] -> 3 (0011) and 4 (0100) do not share bits. Product = 12.
// 3 (0011) and 8 (1000) do not share bits. Product = 24.
// 4 (0100) and 8 (1000) do not share bits. Product = 32.
// 12 (1100) and 3 (0011) do not share bits. Product = 36. Max product is 36.
TEST(MaxProductTest, StandardValidPairs) {
    Solution sol;
    std::vector<int> nums = {3, 4, 8, 12};
    EXPECT_EQ(sol.maxProduct(nums), 36LL);
}

// Test Case 2: Case where no valid pair exists because all elements share at least one bit.
// e.g., nums = [7, 15, 31] -> All have the lowest 3 bits set (111), so they all share common bits.
TEST(MaxProductTest, NoValidPairsExist) {
    Solution sol;
    std::vector<int> nums = {7, 15, 31};
    EXPECT_EQ(sol.maxProduct(nums), 0LL);
}

// Test Case 3: Minimum constraints for array length (nums.length = 2).
TEST(MaxProductTest, MinimumArrayLength) {
    Solution sol;
    
    // Case 3a: The two elements do not share bits.
    std::vector<int> nums1 = {5, 10}; // 5 = 0101, 10 = 1010
    EXPECT_EQ(sol.maxProduct(nums1), 50LL);

    // Case 3b: The two elements share bits.
    std::vector<int> nums2 = {5, 7}; // 5 = 101, 7 = 111
    EXPECT_EQ(sol.maxProduct(nums2), 0LL);
}

// Test Case 4: Array contains duplicate values.
// Duplicates inherently share the exact same set bits (unless the value is 0, but constraints say nums[i] >= 1).
// It should look for distinct indices with non-overlapping bits.
TEST(MaxProductTest, DuplicateElements) {
    Solution sol;
    std::vector<int> nums = {5, 5, 10, 10}; // 5 (0101) and 10 (1010)
    EXPECT_EQ(sol.maxProduct(nums), 50LL);
}

// Test Case 5: Elements with maximum possible value constraint (nums[i] = 10^6).
// 10^6 fits in a standard integer, but the product can be up to 10^12, requiring long long.
// 1,000,000 = 11110100001001000000 (binary)
// We pair it with an element that has non-overlapping bits, e.g., 57 = 00001011101101111111 (inverted mask within range)
TEST(MaxProductTest, MaximumValueConstraints) {
    Solution sol;
    // 1000000 is 0xF4240. An inversion within 20 bits is 0x0BDBF = 48575.
    // 1000000 * 48575 = 48,575,000,000 which fits in long long but overflows 32-bit int.
    std::vector<int> nums = {1000000, 48575};
    EXPECT_EQ(sol.maxProduct(nums), 48575000000LL);
}

// Test Case 6: Multiple pairs are valid, ensuring the algorithm picks the absolute maximum product.
TEST(MaxProductTest, SelectsAbsoluteMaximumProduct) {
    Solution sol;
    // Pairs: 
    // (1, 2) -> product 2 (0001 and 0010)
    // (16, 15) -> product 240 (10000 and 01111)
    std::vector<int> nums = {1, 2, 15, 16};
    EXPECT_EQ(sol.maxProduct(nums), 240LL);
}