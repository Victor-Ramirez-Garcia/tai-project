#include <gtest/gtest.h>
#include <vector>
#include <algorithm>

// Assuming the user's solution is defined here or included via a header
class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, std::value_type target) {
        // Placeholder for the actual solution logic
        return {};
    }
};

// Helper function to verify results since the order of indices in the returned vector can vary
void verifyTwoSum(std::vector<int> result, const std::vector<int>& expected) {
    ASSERT_EQ(result.size(), 2);
    std::sort(result.begin(), result.end());
    std::vector<int> sorted_expected = expected;
    std::sort(sorted_expected.begin(), sorted_expected.end());
    EXPECT_EQ(result, sorted_expected);
}

// --- Example Tests ---

TEST(TwoSumTest, Example1) {
    Solution solution;
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> expected = {0, 1};
    verifyTwoSum(solution.twoSum(nums, target), expected);
}

TEST(TwoSumTest, Example2) {
    Solution solution;
    std::vector<int> nums = {3, 2, 4};
    int target = 6;
    std::vector<int> expected = {1, 2};
    verifyTwoSum(solution.twoSum(nums, target), expected);
}

TEST(TwoSumTest, Example3) {
    Solution solution;
    std::vector<int> nums = {3, 3};
    int target = 6;
    std::vector<int> expected = {0, 1};
    verifyTwoSum(solution.twoSum(nums, target), expected);
}

// --- Edge Cases & Constraints Tests ---

TEST(TwoSumTest, MinimumConstraintsSize) {
    Solution solution;
    std::vector<int> nums = {10, -5};
    int target = 5;
    std::vector<int> expected = {0, 1};
    verifyTwoSum(solution.twoSum(nums, target), expected);
}

TEST(TwoSumTest, NegativeNumbers) {
    Solution solution;
    std::vector<int> nums = {-1, -2, -3, -4, -5};
    int target = -8;
    std::vector<int> expected = {2, 4};
    verifyTwoSum(solution.twoSum(nums, target), expected);
}

TEST(TwoSumTest, LargeValuesAndTarget) {
    Solution solution;
    std::vector<int> nums = {1000000000, -1000000000, 5, 0};
    int target = 0;
    std::vector<int> expected = {0, 1};
    verifyTwoSum(solution.twoSum(nums, target), expected);
}

TEST(TwoSumTest, TargetIsZero) {
    Solution solution;
    std::vector<int> nums = {2, 5, -2, 8};
    int target = 0;
    std::vector<int> expected = {0, 2};
    verifyTwoSum(solution.twoSum(nums, target), expected);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}