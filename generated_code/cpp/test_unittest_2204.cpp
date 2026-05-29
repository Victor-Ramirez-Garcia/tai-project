#include <gtest/gtest.h>
#include <vector>
#include <algorithm>
#include "solution_proxy.h"

// Helper function to validate if the result is a valid subsequence of 'nums' with the correct elements.
// Since multiple valid subsequences can have the same maximum sum, we verify that:
// 1. The result size is exactly k.
// 2. The elements in the result exist in 'nums' in the correct relative order.
// 3. The sum of the elements matches the expected maximum sum.
void VerifyMaxSubsequence(const std::vector<int>& nums, int k, const std::vector<int>& expected_elements, const std::vector<int>& actual_result) {
    ASSERT_EQ(actual_result.size(), k);
    
    // Calculate expected maximum sum from the known best elements
    int expected_sum = 0;
    for (int num : expected_elements) {
        expected_sum += num;
    }
    
    // Calculate actual sum
    int actual_sum = 0;
    for (int num : actual_result) {
        actual_sum += num;
    }
    EXPECT_EQ(actual_sum, expected_sum);

    // Verify it is a valid subsequence of nums
    auto it = nums.begin();
    for (int num : actual_result) {
        it = std::find(it, nums.end(), num);
        ASSERT_NE(it, nums.end()) << "Element " << num << " not found in the remaining subsequence of nums.";
        // Move to the next element for subsequence order maintenance
        std::advance(it, 1);
    }
}

// --- Example Tests ---

TEST(MaxSubsequenceTest, Example1) {
    Solution solution;
    std::vector<int> nums = {2, 1, 3, 3};
    int k = 2;
    std::vector<int> expected = {3, 3};
    std::vector<int> result = solution.maxSubsequence(nums, k);
    VerifyMaxSubsequence(nums, k, expected, result);
}

TEST(MaxSubsequenceTest, Example2) {
    Solution solution;
    std::vector<int> nums = {-1, -2, 3, 4};
    int k = 3;
    std::vector<int> expected = {-1, 3, 4};
    std::vector<int> result = solution.maxSubsequence(nums, k);
    VerifyMaxSubsequence(nums, k, expected, result);
}

TEST(MaxSubsequenceTest, Example3) {
    Solution solution;
    std::vector<int> nums = {3, 4, 3, 3};
    int k = 2;
    // Both [3, 4] and [4, 3] are valid. The helper verifies the sum and subsequence validity.
    std::vector<int> expected = {3, 4}; 
    std::vector<int> result = solution.maxSubsequence(nums, k);
    VerifyMaxSubsequence(nums, k, expected, result);
}

// --- Edge Cases & Constraint Tests ---

TEST(MaxSubsequenceTest, MinimumInputSizeAndK) {
    Solution solution;
    std::vector<int> nums = {42};
    int k = 1;
    std::vector<int> expected = {42};
    std::vector<int> result = solution.maxSubsequence(nums, k);
    VerifyMaxSubsequence(nums, k, expected, result);
}

TEST(MaxSubsequenceTest, KEqualsNumsLength) {
    Solution solution;
    std::vector<int> nums = {10, -5, 20, -1};
    int k = 4;
    std::vector<int> expected = {10, -5, 20, -1};
    std::vector<int> result = solution.maxSubsequence(nums, k);
    VerifyMaxSubsequence(nums, k, expected, result);
}

TEST(MaxSubsequenceTest, AllNegativeNumbers) {
    Solution solution;
    std::vector<int> nums = {-10, -5, -20, -1, -3};
    int k = 2;
    std::vector<int> expected = {-5, -1};
    std::vector<int> result = solution.maxSubsequence(nums, k);
    VerifyMaxSubsequence(nums, k, expected, result);
}

TEST(MaxSubsequenceTest, AllIdenticalNumbers) {
    Solution solution;
    std::vector<int> nums = {5, 5, 5, 5, 5};
    int k = 3;
    std::vector<int> expected = {5, 5, 5};
    std::vector<int> result = solution.maxSubsequence(nums, k);
    VerifyMaxSubsequence(nums, k, expected, result);
}

TEST(MaxSubsequenceTest, LargeNegativeAndPositiveValues) {
    Solution solution;
    std::vector<int> nums = {-100000, 100000, -50000, 75000, 0};
    int k = 3;
    std::vector<int> expected = {100000, 75000, 0};
    std::vector<int> result = solution.maxSubsequence(nums, k);
    VerifyMaxSubsequence(nums, k, expected, result);
}

TEST(MaxSubsequenceTest, DuplicateMaxValuesPreserveCorrectOrder) {
    Solution solution;
    std::vector<int> nums = {1, 2, 3, 2, 3, 1};
    int k = 3;
    // The largest elements are 3, 3, and one of the 2s. 
    // Subsequence must strictly adhere to the relative order of picked elements.
    std::vector<int> expected = {3, 2, 3}; 
    std::vector<int> result = solution.maxSubsequence(nums, k);
    VerifyMaxSubsequence(nums, k, expected, result);
}

TEST(MaxSubsequenceTest, MaximumConstraintsLength) {
    Solution solution;
    std::vector<int> nums(1000, -100);
    // Set exactly 5 elements to the maximum upper bound
    nums[100] = 100000;
    nums[300] = 100000;
    nums[500] = 100000;
    nums[700] = 100000;
    nums[900] = 100000;
    int k = 5;
    
    std::vector<int> expected = {100000, 100000, 100000, 100000, 100000};
    std::vector<int> result = solution.maxSubsequence(nums, k);
    VerifyMaxSubsequence(nums, k, expected, result);
}