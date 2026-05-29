#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

// Test case for the provided example in the problem statement
TEST(SolutionTest, ExampleCase) {
    Solution sol;
    EXPECT_EQ(sol.minOperations("dog"), 1);
}

// Test case for strings that are already sorted
TEST(SolutionTest, AlreadySortedCases) {
    Solution sol;
    EXPECT_EQ(sol.minOperations("a"), 0);
    EXPECT_EQ(sol.minOperations("abc"), 0);
    EXPECT_EQ(sol.minOperations("aabbcc"), 0);
}

// Test case where the string can be sorted in exactly 1 operation
// (i.e., the first character is the smallest or the last character is the largest)
TEST(SolutionTest, SingleOperationCases) {
    Solution sol;
    // First character 'a' is the minimum, we can sort the rest "cba" -> "abc"
    EXPECT_EQ(sol.minOperations("acba"), 1);
    // Last character 'z' is the maximum, we can sort the rest "cba" -> "abc"
    EXPECT_EQ(sol.minOperations("cbaz"), 1);
}

// Test case where the string requires 2 operations
// (i.e., the string is not sorted, but the minimum isn't at the start and the maximum isn't at the end)
TEST(SolutionTest, TwoOperationsCases) {
    Solution sol;
    EXPECT_EQ(sol.minOperations("bca"), 2);
    EXPECT_EQ(sol.minOperations("dcba"), 2);
}

// Test case handling duplicates and edge patterns
TEST(SolutionTest, DuplicateCharacters) {
    Solution sol;
    EXPECT_EQ(sol.minOperations("baaa"), 1);
    EXPECT_EQ(sol.minOperations("aaab"), 0);
    EXPECT_EQ(sol.minOperations("baba"), 1);
}

// Test case exploring the minimum constraint length
TEST(SolutionTest, MinimumLengthConstraint) {
    Solution sol;
    EXPECT_EQ(sol.minOperations("z"), 0);
    EXPECT_EQ(sol.minOperations("ba"), 1);
    EXPECT_EQ(sol.minOperations("ab"), 0);
}