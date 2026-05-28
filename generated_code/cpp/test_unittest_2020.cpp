#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Test Case: Example 1 from the problem description
TEST(CanBeIncreasingTest, Example1_ValidRemovalInMiddle) {
    Solution solution;
    std::vector<int> nums = {1, 2, 10, 5, 7};
    EXPECT_TRUE(solution.canBeIncreasing(nums));
}

// Test Case: Example 2 from the problem description
TEST(CanBeIncreasingTest, Example2_InvalidMultipleDrops) {
    Solution solution;
    std::vector<int> nums = {2, 3, 1, 2};
    EXPECT_FALSE(solution.canBeIncreasing(nums));
}

// Test Case: Example 3 from the problem description
TEST(CanBeIncreasingTest, Example3_AllIdenticalElements) {
    Solution solution;
    std::vector<int> nums = {1, 1, 1};
    EXPECT_FALSE(solution.canBeIncreasing(nums));
}

// Edge Case: Minimum allowed array length by constraints (nums.length == 2)
// Removing any single element from a 2-element array always leaves 1 element, which is strictly increasing.
TEST(CanBeIncreasingTest, EdgeCase_MinimumLengthTwo) {
    Solution solution;
    std::vector<int> nums1 = {10, 1};
    std::vector<int> nums2 = {5, 5};
    std::vector<int> nums3 = {1, 2};
    EXPECT_TRUE(solution.canBeIncreasing(nums1));
    EXPECT_TRUE(solution.canBeIncreasing(nums2));
    EXPECT_TRUE(solution.canBeIncreasing(nums3));
}

// Edge Case: Array is already strictly increasing (0 removals needed)
TEST(CanBeIncreasingTest, EdgeCase_AlreadyStrictlyIncreasing) {
    Solution solution;
    std::vector<int> nums = {1, 2, 3, 4, 5};
    EXPECT_TRUE(solution.canBeIncreasing(nums));
}

// Edge Case: Peak element at the very beginning requires removal
TEST(CanBeIncreasingTest, EdgeCase_RemoveAtStart) {
    Solution solution;
    std::vector<int> nums = {10, 1, 2, 3};
    EXPECT_TRUE(solution.canBeIncreasing(nums));
}

// Edge Case: Drop occurs at the very end requiring removal of the last element
TEST(CanBeIncreasingTest, EdgeCase_RemoveAtEnd) {
    Solution solution;
    std::vector<int> nums = {1, 2, 3, 0};
    EXPECT_TRUE(solution.canBeIncreasing(nums));
}

// Scenario: A single duplicate pair that can be resolved by removing one of them
TEST(CanBeIncreasingTest, Scenario_SingleDuplicatePair) {
    Solution solution;
    std::vector<int> nums = {1, 2, 2, 3};
    EXPECT_TRUE(solution.canBeIncreasing(nums));
}

// Scenario: Modification requires checking nums[i] vs nums[i-2] logic 
// Case A: Must remove nums[i] (e.g., [1, 3, 5, 4, 7] -> remove 4, but 5 >= 4. Since 3 < 7, removing 4 works)
TEST(CanBeIncreasingTest, Scenario_RemoveCurrentElement) {
    Solution solution;
    std::vector<int> nums = {1, 3, 5, 4, 7};
    EXPECT_TRUE(solution.canBeIncreasing(nums));
}

// Case B: Must remove nums[i-1] (e.g., [1, 4, 2, 3] -> remove 4 because 4 >= 2 and 1 < 2)
TEST(CanBeIncreasingTest, Scenario_RemovePreviousElement) {
    Solution solution;
    std::vector<int> nums = {1, 4, 2, 3};
    EXPECT_TRUE(solution.canBeIncreasing(nums));
}

// Edge Case: Maximum constraints check (Large strictly increasing array)
TEST(CanBeIncreasingTest, EdgeCase_MaximumConstraintsValid) {
    Solution solution;
    std::vector<int> nums;
    for (int i = 1; i <= 1000; ++i) {
        nums.push_back(i);
    }
    EXPECT_TRUE(solution.canBeIncreasing(nums));
}